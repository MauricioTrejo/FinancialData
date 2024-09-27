# Stocks.py
import requests
import pandas as pd
import logging

class Stock:
    def __init__(self, api_key: str, symbol_list: list):
        """
        Initializes the Stock class with the API key and symbol(s).

        Args:
            symbol list: A list of stock symbols.
                Ex. ['AAPL', 'GOOGL', 'MSFT']
        """
        self.api_key = api_key
        self.symbol_list = symbol_list

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def get_company_profile(self) -> pd.DataFrame:
        """
        Retrieves company profile data for a specified symbol.
        
        Returns:
            pd.DataFrame: A DataFrame containing the company profile data.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        # Creating an empty DataFrame to store the data
        companies_df = pd.DataFrame()

        for stock_symbol in symbol:
            # Construct the API URL
            url = f'https://financialmodelingprep.com/api/v3/profile/{stock_symbol}?apikey={self.api_key}'
        
            # Retrieve company profile data from the API
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            company_df = pd.DataFrame(data)

            # Concatenate data for multiple stock symbols
            if companies_df.empty:
                companies_df = company_df
            else:
                companies_df = pd.concat([companies_df, company_df], ignore_index=True)

            # Updating status of data retrieved
            self.logger.info(f'Company profile for {stock_symbol} successfully retrieved')
        
        return companies_df
    
    def get_income_statement(self, as_reported: bool, period: str) -> pd.DataFrame:
        """
        Retrieves income statement data for a specified period.

        Args:
            as_reported bool: True to retrieve as reported by the company or False for adjusted financials.
            
            period str: The period for which the income statement data is required.
                Ex. 'annual', 'quarter'.

        Returns:
            pd.DataFrame: A DataFrame containing the income statement data.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        # Creating an empty DataFrame to store the data
        income_statement_df = pd.DataFrame()

        for stock_symbol in self.symbol_list:
            # Construct the API URL
            if as_reported:
                url = f'https://financialmodelingprep.com/api/v3/income-statement-as-reported/{stock_symbol}?period={period}&apikey={self.api_key}'
            else:
                url = f'https://financialmodelingprep.com/api/v3/income-statement/{stock_symbol}?period={period}&apikey={self.api_key}'
            
            # Retrieve income statement data from the API
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            income_df = pd.DataFrame(data)

            # Concatenate data for multiple stock symbols
            if income_statement_df.empty:
                income_statement_df = income_df
            else:
                income_statement_df = pd.concat([income_statement_df, income_df], ignore_index=True)

            # Updating status of data retrieved
            self.logger.info(f'Income statement for {stock_symbol} successfully retrieved')
        
        return income_statement_df
    
    def get_balance_sheet(self, as_reported: bool, period: str) -> pd.DataFrame:
        """
        Retrieves balance sheet data for a specified period.

        Args:
            as_reported bool: True to retrieve as reported by the company or False for adjusted financials.
            
            period str: The period for which the balance sheet data is required.
                Ex. 'annual', 'quarter'.

        Returns:
            pd.DataFrame: A DataFrame containing the balance sheet data.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        # Creating an empty DataFrame to store the data
        balance_sheet_df = pd.DataFrame()

        for stock_symbol in self.symbol_list:
            # Construct the API URL
            if as_reported:
                url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/{stock_symbol}?period={period}&apikey={self.api_key}'
            else:
                url = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock_symbol}?period={period}&apikey={self.api_key}'
            
            # Retrieve balance sheet data from the API
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            balance_df = pd.DataFrame(data)

            # Concatenate data for multiple stock symbols
            if balance_sheet_df.empty:
                balance_sheet_df = balance_df
            else:
                balance_sheet_df = pd.concat([balance_sheet_df, balance_df], ignore_index=True)

            # Updating status of data retrieved
            self.logger.info(f'Balance sheet for {stock_symbol} successfully retrieved')
        
        return balance_sheet_df
    
    def get_cash_flow_statement(self, as_reported: bool, period: str) -> pd.DataFrame:
        """
        Retrieves cash flow statement data for a specified period.

        Args:
            as_reported bool: True to retrieve as reported by the company or False for adjusted financials.
            
            period str: The period for which the cash flow statement data is required.
                Ex. 'annual', 'quarter'.

        Returns:
            pd.DataFrame: A DataFrame containing the cash flow statement data.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        # Creating an empty DataFrame to store the data
        cash_flow_df = pd.DataFrame()

        for stock_symbol in self.symbol_list:
            # Construct the API URL
            if as_reported:
                url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement-as-reported/{stock_symbol}?period={period}&apikey={self.api_key}'
            else:
                url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{stock_symbol}?period={period}&apikey={self.api_key}'
            
            # Retrieve cash flow statement data from the API
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            cash_df = pd.DataFrame(data)

            # Concatenate data for multiple stock symbols
            if cash_flow_df.empty:
                cash_flow_df = cash_df
            else:
                cash_flow_df = pd.concat([cash_flow_df, cash_df], ignore_index=True)

            # Updating status of data retrieved
            self.logger.info(f'Cash flow statement for {stock_symbol} successfully retrieved')
        
        return cash_flow_df