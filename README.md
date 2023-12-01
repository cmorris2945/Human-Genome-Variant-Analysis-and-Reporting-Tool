# Human Genome Variant Analysis and Reporting Tool

## Description
The Human Genome Variant Analysis and Reporting Tool is a Python-based application designed for analyzing VCF (Variant Call Format) files mapped to the human_g1k_v37 reference. It extracts and reports detailed information about each genomic variant, including chromosome, position, alleles, coverage depth, gene name, variant effect, and more. The tool leverages Ensembl REST services to enrich the variant data, providing comprehensive insights into each variant's nature and potential impact.

## Features
- Parse VCF files to extract variant information.
- Retrieve additional variant details using the Ensembl REST API.
- Output a comprehensive report in CSV format, including fields like:
  - Chromosome
  - Position
  - Reference Allele
  - Alternate Allele
  - Coverage Depth
  - Read Counts
  - Allele Frequencies
  - Gene Names
  - Variant Effects
  - Somatic Variant Indicators
  - Cosmic IDs and rsIDs

## Prerequisites
- Python 3.x
- import requests
- import csv
- import sys

## Installation
1. Clone the repository:
2. Set up your IDE.
3. Add the test_vcf.txt file to program to extract relevant features.

![image](https://github.com/cmorris2945/Human-Genome-Variant-Analysis-and-Reporting-Tool/assets/30676606/e6be77d6-2282-45d0-bc39-15eccbce89a0)



![image](https://github.com/cmorris2945/Human-Genome-Variant-Analysis-and-Reporting-Tool/assets/30676606/42c8b190-659c-4282-b204-9b79ade22659)


