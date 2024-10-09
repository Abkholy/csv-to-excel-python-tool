# CSV to Excel Converter

This script converts CSV files to Excel files with multiple sheets if the number of rows exceeds a specified limit.

## Requirements

- Python 3.x
- pandas
- xlsxwriter

## Installation

1. Install the required Python packages:

    ```sh
    pip install pandas xlsxwriter
    ```

2. Ensure your directory structure is similar to the following:

    ```
    2022 File/
        2022 File.csv
        2022 File.xlsx
    2023 File/
        01 TO  06 -  2023  File.csv
        01 TO  06 -  2023  File.xlsx
        07 - 2023 File.csv
        08 - 2023 File.csv
        09 - 2023 File.csv
        10 - 2023 File.csv
        11 - 2023 File.csv
        12 - 2023 File.csv
    2024  File/
        01- 2024 File.csv
        02 - 2024 File.csv
        03- 2024 File.csv
        04- 2024 File.csv
        05- 2024 File.csv
        06- 2024 File.csv
        07- 2024 File.csv
    ```

## Usage

1. Open a terminal and navigate to the directory containing `index.py`.

2. Run the script:

    ```sh
    python index.py
    ```

3. The script will iterate through all CSV files in the specified directory and convert them to Excel files with multiple sheets if necessary.

## Configuration

- You can change the directory path and the maximum number of rows per sheet by modifying the `directory` and `max_rows_per_sheet` variables in `index.py`.

    ```python
    directory = './'  # Replace with your directory path
    max_rows_per_sheet = 500000  # Adjust as needed
    ```

## Example

The script will convert CSV files in the specified directory to Excel files. For example, `2022 File/2022 File.csv` will be converted to `2022 File/2022 File.xlsx`.

## License

This project is licensed under the MIT License.