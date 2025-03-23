# FluBarcoding/cli.py

import argparse
from flubarcode import preprocessing, feature_extraction, barcode_testing, visualization
# from FluBarcoding import feature_extraction, barcode_testing, visualization

def main():
    parser = argparse.ArgumentParser(description='flubarcode: A package for barcode sequencing data processing and analysis')
    subparsers = parser.add_subparsers(dest='command')

    qc_parser = subparsers.add_parser('qc', help='Run quality control')
    qc_parser.add_argument('input_file', help='Input file for quality control')
    qc_parser.add_argument('output_dir', help='Output directory for quality control results')

    fe_parser = subparsers.add_parser('fe', help='Feature extraction')
    fe_parser.add_argument('input_file', help='Input file for feature extraction')
    fe_parser.add_argument('output_file', help='Output file for feature extraction results')

    bt_parser = subparsers.add_parser('bt', help='Barcode testing')
    bt_parser.add_argument('true_positives', type=int, help='Number of true positives')
    bt_parser.add_argument('false_negatives', type=int, help='Number of false negatives')
    bt_parser.add_argument('true_negatives', type=int, help='Number of true negatives')
    bt_parser.add_argument('false_positives', type=int, help='Number of false positives')

    vis_parser = subparsers.add_parser('vis', help='Data visualization')
    vis_parser.add_argument('input_file', help='Input file for visualization')
    vis_parser.add_argument('output_file', help='Output file for visualization results')

    args = parser.parse_args()

    if args.command == 'qc':
        preprocessing.run_fastqc(args.input_file, args.output_dir)
    elif args.command == 'fe':
        feature_extraction.calculate_gc_content(args.input_file)
    elif args.command == 'bt':
        recall = barcode_testing.calculate_recall_rate(args.true_positives, args.false_negatives)
        specificity = barcode_testing.calculate_specificity(args.true_negatives, args.false_positives)
        print(f"Recall Rate: {recall}, Specificity: {specificity}")
    elif args.command == 'vis':
        visualization.plot_gc_content(args.input_file, args.output_file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
