import pandas as pd
import os
import math

def split_csv_to_excel_sheets(directory, max_rows_per_sheet=500000):
    # Iterate over all files and folders in the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Check if the file is a CSV file
            if filename.endswith(".csv"):
                csv_file = os.path.join(root, filename)
                excel_file = os.path.join(root, filename.replace(".csv", ".xlsx"))

                # Read the CSV file into a DataFrame
                df = pd.read_csv(csv_file)

                # Calculate the number of sheets needed
                num_sheets = math.ceil(len(df) / max_rows_per_sheet)
                print(f"Converting '{csv_file}' to '{excel_file}'...")
                print(f"Number of rows: {len(df)}")
                print(f"Max rows per sheet: {max_rows_per_sheet}")
                print(f"Number of sheets: {num_sheets}")

                # Create an Excel writer object
                with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
                    for i in range(num_sheets):
                        start_row = i * max_rows_per_sheet
                        end_row = start_row + max_rows_per_sheet
                        sheet_name = f'Sheet{i+1}'
                        df.iloc[start_row:end_row].to_excel(writer, sheet_name=sheet_name, index=False)
                        print(f"Written '{sheet_name}' with rows {start_row} to {end_row} in '{filename.replace('.csv', '.xlsx')}'")

                print(f"Converted '{csv_file}' to '{excel_file}' with {num_sheets} sheets.")

# Example usage:
directory = './'  # Replace with your directory path
split_csv_to_excel_sheets(directory)
