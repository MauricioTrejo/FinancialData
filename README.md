# Financial Data Retrieval Library
A Python library for retrieving financial data from the [Financial Modeling Prep API](https://site.financialmodelingprep.com/developer/docs). This library provides classes to fetch data on various financial instruments (stocks, ETFs, funds, trusts) and detailed company data for specified stock symbols.

# Table of Contents
- Features
- Getting Started
- Usage
- Logging
- Contact

## Features
- Retrieve lists of financial instruments filtered by type and exchange.
- Fetch company profiles for specific stock symbols.
- Obtain financial statements (income statement, balance sheet, cash flow statement) for stocks, with options for as-reported or adjusted data and different periods (annual or quarterly).

## Getting Started
**Prerequisites**
- Python 3.6 or higher
- An API key from Financial Modeling Prep
**API Key Setup**
1. Sign up for an API key [here](https://site.financialmodelingprep.com/developer/docs).
2. Store your API key securely. It's recommended to set it as an environment variable or use a configuration file that's not checked into version control.

## Usage
**Instruments Class**
The Instruments class allows you to retrieve data on various financial instruments filtered by type and exchange.
```
import pandas as pd
from Instruments import Instruments

# Initialize the Instruments class with your API key
api_key = 'your_api_key_here'
instruments = Instruments(api_key)

# Define the instrument types and exchanges you're interested in
instrument_types = ['stock', 'etf']
exchanges = ['NASDAQ', 'NYSE']

# Fetch the instruments data
instruments_df = instruments.get_instruments(instrument_types, exchanges)

# Display the data
print(instruments_df.head())
```
**Stock Class**
The Stock class provides methods to retrieve company profiles and financial statements for specified stock symbols.
```
import pandas as pd
from Stocks import Stock

# Initialize the Stock class with your API key and a list of stock symbols
api_key = 'your_api_key_here'
symbols = ['AAPL', 'MSFT', 'GOOGL']
stock_data = Stock(api_key, symbols)

# Retrieve company profiles
profiles_df = stock_data.get_company_profile(symbols)
print(profiles_df.head())

# Retrieve income statements (as reported, annual)
income_statements_df = stock_data.get_income_statement(as_reported=True, period='annual')
print(income_statements_df.head())

# Retrieve balance sheets (adjusted, quarterly)
balance_sheets_df = stock_data.get_balance_sheet(as_reported=False, period='quarter')
print(balance_sheets_df.head())

# Retrieve cash flow statements (adjusted, annual)
cash_flow_statements_df = stock_data.get_cash_flow_statement(as_reported=False, period='annual')
print(cash_flow_statements_df.head())
```
## Logging
The classes use Python's built-in logging module to provide informational messages about the data retrieval process. By default, logging is set to the INFO level. You can adjust the logging level as needed:
```
import logging

# Set logging level to DEBUG to see more detailed output
logging.basicConfig(level=logging.DEBUG)
```
## Contact
If you have any questions or need further assistance, feel free to reach out:

Email: mtrejosantamaria@gmail.com
GitHub: MauricioTrejo
