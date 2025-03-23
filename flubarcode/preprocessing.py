# FluBarcoding/preprocessing.py

import subprocess
from Bio import SeqIO

def run_fastqc(input_file, output_dir):
    subprocess.run(['fastqc', input_file, '-o', output_dir])

def filter_low_quality_sequences(input_file, output_file, quality_threshold):
    with open(output_file, 'w') as out_handle:
        for record in SeqIO.parse(input_file, 'fastq'):
            if min(record.letter_annotations["phred_quality"]) >= quality_threshold:
                SeqIO.write(record, out_handle, 'fastq')

def remove_adapters(input_file, output_file, adapter_sequence):
    # Placeholder for adapter removal implementation
    pass

def merge_sequences(fasta_file, qual_file, output_file):
    from Bio.SeqIO.QualityIO import PairedFastaQualIterator
    from Bio.Seq import Seq

    with open(fasta_file) as fasta_handle, open(qual_file) as qual_handle:
        sequences = PairedFastaQualIterator(fasta_handle, qual_handle)
        with open(output_file, 'w') as out_handle:
            for record in sequences:
                record.seq = Seq(str(record.seq).replace('N', ''))
                SeqIO.write(record, out_handle, 'fastq')

def trim_sequences(input_file, output_file, trim_length):
    with open(output_file, 'w') as out_handle:
        for record in SeqIO.parse(input_file, 'fastq'):
            trimmed_record = record[:trim_length]
            SeqIO.write(trimmed_record, out_handle, 'fastq')

def convert_format(input_file, output_file, input_format, output_format):
    records = SeqIO.parse(input_file, input_format)
    SeqIO.write(records, output_file, output_format)
