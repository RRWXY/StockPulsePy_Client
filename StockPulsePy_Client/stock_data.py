import requests
import os
import pandas as pd

from .api_initialization import ApiInitialize

class StockData:
    def __init__(self, api_client):
        self.api_client = api_client
        
    def get_esg_score(self, symbol, **kwargs):
        """
        Get ESG (Environmental, Social, and Governance) score for a given symbol.

        Args:
            symbol (str): Stock symbol
            **kwargs: Additional optional keyword arguments.

        Returns:
            dict: ESG score results
        """
        url = f"https://stockpulse1.p.rapidapi.com/esg-score/{symbol}"
        params = kwargs  # Add any additional parameters to the request
        try:
            response = requests.get(url, headers=self.api_client.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching ESG score: {e}")
            return {}


    def get_stock_price(self, ticker='tsla', **kwargs):
        """
        Get stock price for a given ticker.

        Args:
            ticker (str): Stock ticker symbol, default is 'tsla'.
            **kwargs: Additional optional keyword arguments.

        Returns:
            dict: Stock price results
        """
        params = {'ticker': ticker}
        params.update(kwargs)  # Update params with any additional keyword arguments
        url = f"https://stockpulse1.p.rapidapi.com/price/{ticker}"
        try:
            response = requests.get(url, headers=self.api_client.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data  
        except requests.RequestException as e:
            print(f"Error fetching stock price: {e}")
            return {}

    
