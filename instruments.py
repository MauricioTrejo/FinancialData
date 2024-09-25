# Instruments.py
import requests
import pandas as pd
import logging

class Instruments:
    def __init__(self, api_key: str):
        self.api_key = api_key
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_instruments(self, instruments: list, exchanges: list) -> pd.DataFrame:
        """
        Retrieves available instruments data from the API, filtered by instrument types.

        Args:
            instruments list: List of instrument types to include.
                Valid options can be chosen from the following list ['etf', 'fund', 'stock', 'trust'].
            
            exchanges list: List of exchanges to include.
                Ex. NASDAQ, NYSE, AMEX, EURONEXT, etc.
                For valid options consult -> https://site.financialmodelingprep.com/developer/docs

        Returns:
            pd.DataFrame: A DataFrame containing the available instruments data.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        # Valid instrument types
        valid_instruments = {'etf', 'fund', 'stock', 'trust'}

        # Validate the instruments
        invalid_instruments = set(instruments) - valid_instruments
        if invalid_instruments:
            raise ValueError(f"Invalid instrument types provided: {invalid_instruments}")

        # Construct the API URL
        url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey={self.api_key}"
        
        # Retrieve available instruments data from the API
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful

        data = response.json()
        instruments_df = pd.DataFrame(data)

        # Filter data for the specified instruments
        instruments_df = instruments_df[instruments_df.type.isin(instruments)]

        # Filter data for specified exchanges
        instruments_df = instruments_df[instruments_df.exchangeShortName.isin(exchanges)]

        return instruments_df