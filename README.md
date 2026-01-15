# Small Business Analysis - Coffee Shop Demo

This project provides a complete pipeline for generating synthetic sales data for a small coffee shop and performing a deep Exploratory Data Analysis (EDA) with professional visualizations.

## Project Overview

The goal of this project is to simulate a year's worth of coffee shop transactions and analyze business performance, including revenue trends, product popularity, and peak operating hours.

## Features

- **Data Generation**: A custom script that simulates realistic sales patterns, including morning peaks, weighted product popularity, and varying customer types.
- **Deep Analysis**: Financial reporting (Total Revenue, Average Transaction Value), Category performance, and Peak hour identification.
- **Visualizations**: Automatically generates five key business charts:
  - Monthly Revenue Trend
  - Sales by Category
  - Hourly Transaction Volume
  - Top 10 Best-Selling Items
  - Payment Method Distribution

## Project Structure

```text
small-business-analysis/
├── coffee_shop_sales.csv     # The generated dataset (after running script)
├── generate_data.py          # Script to create the synthetic data
├── analyze_data.py           # Script to perform EDA and save plots
├── visualizations/           # Folder containing generated PNG charts
└── README.md                 # Project documentation
```

## Setup & Installation

### Prerequisites

Ensure you have Python 3.x installed. This project uses the following libraries:
- `pandas`
- `matplotlib`
- `seaborn`

### Installation

Install the required dependencies using pip:

```powershell
pip install pandas matplotlib seaborn
```

## How to Run

1. **Generate the Data**:
   Run the generation script to create the `coffee_shop_sales.csv` file.
   ```powershell
   python generate_data.py
   ```

2. **Run Analysis**:
   Run the analysis script to process the data and generate visualizations in the `visualizations/` folder.
   ```powershell
   python analyze_data.py
   ```

## Key Insights (Sample)

- **Total Revenue**: ~$102,000 annually.
- **Peak Hour**: 9:00 AM (Morning rush).
- **Highest Revenue Product**: Avocado Toast (Premium food item).
- **Most Popular Product**: Cappuccino (Highest volume).
- **Dominant Category**: Coffee (Accounts for nearly 43% of revenue).

## License

This project is open-source and available under the MIT License.
