# main.py

import argparse
from ecs_report import generate_report

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="CLI tool for generating ECS resource reports."
    )
    
    # Add arguments
    parser.add_argument(
        '--cluster', 
        required=True, 
        type=str, 
        help="Name of the ECS cluster."
    )
    parser.add_argument(
        '--output-format', 
        choices=['json', 'csv'], 
        required=True, 
        help="Format of the output report (json or csv)."
    )
    parser.add_argument(
        '--file-path', 
        required=False, 
        type=str, 
        help="Path to save the generated report."
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Validate arguments
    if args.output_format == 'csv' and not args.file_path:
        print("Error: --file-path is required when --output-format is 'csv'.")
        exit(1)
    
    # Generate the report
    try:
        generate_report(args.cluster, args.output_format, args.file_path)
        if args.file_path:
            print(f"Report generated successfully at {args.file_path}")
    except Exception as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    main()