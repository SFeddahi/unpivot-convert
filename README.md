# Unpivot enriched product data

## Overview

**Unpivot-Convert** is a Python script designed to streamline the transformation of Excel product data from a long (unpivoted) format to a wide format. In the original data structure, multiple rows are used for each unique identifier (EAN, SKU, etc.), along with associated categories and values. The script reshapes this data into a more traditional pivoted format, where each unique identifier has its own row, and categories are represented as separate columns.

## Features

- **Data Reshaping:** Converts long-format Excel product data into a wide-format for improved readability and analysis.
- **Enriched/Existing Values:** The script intelligently handles enriched/existing values during the conversion process, ensuring that prior data enrichment is seamlessly incorporated into the transformed dataset.
- **Ease of Analysis:** Facilitates easy analysis of product data with a structured and intuitive layout.

