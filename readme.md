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
    [index.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5CAbdelrahman%20Essam%5C%5CDocuments%5C%5C%D8%AC%D9%85%D9%8A%D8%B9%20%D8%A7%D9%84%D8%AA%D8%AD%D8%B5%D9%8A%D9%84%D8%A7%D8%AA%20DAHWA%5C%5Cindex.py%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAbdelrahman%20Essam%2FDocuments%2F%D8%AC%D9%85%D9%8A%D8%B9%20%D8%A7%D9%84%D8%AA%D8%AD%D8%B5%D9%8A%D9%84%D8%A7%D8%AA%20DAHWA%2Findex.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
    [readme.md](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5CAbdelrahman%20Essam%5C%5CDocuments%5C%5C%D8%AC%D9%85%D9%8A%D8%B9%20%D8%A7%D9%84%D8%AA%D8%AD%D8%B5%D9%8A%D9%84%D8%A7%D8%AA%20DAHWA%5C%5Creadme.md%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAbdelrahman%20Essam%2FDocuments%2F%D8%AC%D9%85%D9%8A%D8%B9%20%D8%A7%D9%84%D8%AA%D8%AD%D8%B5%D9%8A%D9%84%D8%A7%D8%AA%20DAHWA%2Freadme.md%22%2C%22scheme%22%3A%22file%22%7D%7D)
    ```

## Usage

1. Open a terminal and navigate to the directory containing `index.py`.

2. Run the script:

    ```sh
    python [index.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5CAbdelrahman%20Essam%5C%5CDocuments%5C%5C%D8%AC%D9%85%D9%8A%D8%B9%20%D8%A7%D9%84%D8%AA%D8%AD%D8%B5%D9%8A%D9%84%D8%A7%D8%AA%20DAHWA%5C%5Cindex.py%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2FC%3A%2FUsers%2FAbdelrahman%20Essam%2FDocuments%2F%D8%AC%D9%85%D9%8A%D8%B9%20%D8%A7%D9%84%D8%AA%D8%AD%D8%B5%D9%8A%D9%84%D8%A7%D8%AA%20DAHWA%2Findex.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
    ```

3. The script will iterate through all CSV files in the specified directory and convert them to Excel files with multiple sheets if necessary.

## Configuration

- You can change the directory path and the maximum number of rows per sheet by modifying the `directory` and `max_rows_per_sheet` variables in `index.py`.

    ```python
    directory = './'  # Replace with your directory path
    max_rows_per_sheet = 500000  # Adjust as needed
    ```

## Example

The script will convert CSV files in the specified directory to Excel files. For example, `2022 DAHWA/2022 DAHWA.csv` will be converted to `2022 DAHWA/2022 DAHWA.xlsx`.

## License

This project is licensed under the MIT License.