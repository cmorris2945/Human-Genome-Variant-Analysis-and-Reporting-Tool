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

