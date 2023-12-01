import requests
import csv
import sys

# Function to parse the VCF file and extract relevant information
def extract_vcf_data(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):  # Skip header lines
                parts = line.strip().split('\t')
                chrom, pos, _, ref, alts, _, _, info, _, sample_info = parts
                info_data = {item.split('=')[0]: item.split('=')[1] for item in info.split(';') if '=' in item}
                depth = int(info_data.get('TC', 0))
                alt_reads_list = sample_info.split(':')[-1].split(',')

                for alt_idx, alt in enumerate(alts.split(',')):
                    alt_reads = int(alt_reads_list[alt_idx]) if alt_idx < len(alt_reads_list) else 0
                    percent_alt_reads = (alt_reads / depth * 100) if depth else 0
                    percent_ref_reads = ((depth - alt_reads) / depth * 100) if depth else 0

                    yield {
                        'chrom': chrom,
                        'pos': pos,
                        'ref': ref,
                        'alt': alt,
                        'depth': depth,
                        'alt_reads': alt_reads,
                        'percent_alt_reads': percent_alt_reads,
                        'percent_ref_reads': percent_ref_reads
                    }

# Function to query the Ensembl VEP (Variant Effect Predictor) API
def query_ensembl_vep(chrom, pos, ref, alt):
    url = "http://grch37.rest.ensembl.org/vep/human/region"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "variants": [f"{chrom} {pos} . {ref} {alt} . . ."]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json() if response.ok else None

# Function to process the VEP API response and extract needed information
def process_vep_response(api_response):
    gene_names = set()
    for consequence in api_response[0].get('transcript_consequences', []):
        if 'gene_symbol' in consequence:
            gene_names.add(consequence['gene_symbol'])

    gene_name = ', '.join(gene_names)
    variant_effect = api_response[0].get('most_severe_consequence', '')

    colocated_variants = api_response[0].get('colocated_variants', [])
    somatic_variant = ''
    cosmic_id = ''
    rsid = ''
    minor_allele = ''
    minor_allele_freq = ''

    for variant in colocated_variants:
        if variant.get('somatic'):
            somatic_variant = '1'
            cosmic_id = variant.get('id', '')
        else:
            rsid = variant.get('id', '')
            minor_allele = variant.get('minor_allele', '')
            minor_allele_freq = variant.get('minor_allele_freq', '')

    return {
        'gene_name': gene_name,
        'variant_effect': variant_effect,
        'minor_allele': minor_allele,
        'minor_allele_frequency': minor_allele_freq,
        'somatic': somatic_variant,
        'id': cosmic_id if somatic_variant else rsid
    }

# Main execution function
def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_vcf_file> <output_csv_file>")
        sys.exit(1)

    vcf_file_path = sys.argv[1]
    output_csv_path = sys.argv[2]

    vcf_data = list(extract_vcf_data(vcf_file_path))
    processed_data = []

    for record in vcf_data:
        api_response = query_ensembl_vep(record['chrom'], record['pos'], record['ref'], record['alt'])
        if api_response:
            vep_data = process_vep_response(api_response)
            record.update(vep_data)
        else:
            record.update({
                'gene_name': '',
                'variant_effect': '',
                'minor_allele': '',
                'minor_allele_frequency': '',
                'somatic': '',
                'id': ''
            })

        processed_data.append(record)

    keys = processed_data[0].keys()
    with open(output_csv_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(processed_data)

if __name__ == "__main__":
    main()