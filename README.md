# Unpivot-Convert: Excel Product Data Transformation

## Overview

**Unpivot-Convert** is a Python script designed to streamline the transformation of Excel product data from a long (unpivoted) format to a wide format. In the original data structure, multiple rows are used for each unique identifier (EAN, SKU, etc.), along with associated categories and values. The script reshapes this data into a more traditional pivoted format, where each unique identifier has its own row, and categories are represented as separate columns.

## Features

- **Data Reshaping:** Converts long-format Excel product data into a wide-format for improved readability and analysis.
- **Enriched/Existing Values:** The script intelligently handles enriched/existing values during the conversion process, ensuring that prior data enrichment is seamlessly incorporated into the transformed dataset.
- **Ease of Analysis:** Facilitates easy analysis of product data with a structured and intuitive layout.

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sfeddahi/unpivot-convert.git
   ```

2. **Install the required Python libraries:**

   ```bash
   pip install pandas openpyxl
   ```

3. **Execute the script:**

   ```bash
   python unpivot_convert.py path_to_input_data.xlsx path_to_output_data.xlsx
   ```

   - Replace `path_to_input_data.xlsx` with the path to your source Excel file.
   - Replace `path_to_output_data.xlsx` with the desired path for the resulting pivoted Excel file.

## Example Usage

```bash
# Example usage
# python unpivot_convert.py path/to/input_data.xlsx path/to/output_data.xlsx
```

## Handling Enriched/Existing Values

The script is designed to intelligently handle enriched and existing values during the conversion process. If values have been enriched before the conversion, the script ensures a seamless integration, updating the pivoted dataset with the enriched information.

## Dependencies

- [pandas](https://pandas.pydata.org/): For data manipulation and processing.
- [openpyxl](https://openpyxl.readthedocs.io/): For reading and writing Excel files.

## Contributions

Contributions are welcome! If you encounter any issues or wish to enhance the functionality, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [MIT-LICENSE](https://github.com/SFeddahi/unpivot-convert/blob/b558a50e8872baeb4a61b72e13612f5af8dceabc/MIT-LICENSE) file for details.
```
