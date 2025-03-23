#模块二--条形码片段测试
import Flubarcoding.barcode_testing as bt

# input and output files
input_fasta_path = 'input.fasta'  # Replace with the path to your input FASTA file
barcode_file_path = 'barcodes_input.fasta'  # Replace with the path to your barcode file
output_excel_path = 'output.xlsx'  # Replace with the desired output Excel file path

import Flubarcoding.barcode_testing as bt
# Calculation of recall
bt.process_files_recall(input.fasta, barcodes_input.fasta, output.xlsx)
# Calculation of specificity
bt.process_files_specificity(input.fasta, barcodes_input.fasta, output.xlsx)
# Primers design
bt.process_files_primers(barcodes_input.fasta, output.xlsx)


