import requests
import os
import pandas as pd

from .api_initialization import ApiInitialize

class AnalyticsData:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_search_results(self, query='aa', **kwargs):
        """
        Search for a given query.

        Args:
            query (str): Search query

        Returns:
            dict: Search results
        """
        url = f"https://stockpulse1.p.rapidapi.com/search/{query}"
        params = kwargs
        try:
            response = requests.get(url, headers=self.api_client.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching search results: {e}")
            return {}

    def get_analytics_results(self, ticker='tsla', **kwargs):
        """
        Get finance analytics for a given ticker.

        Args:
            ticker (str): Stock ticker symbol, default is 'tsla'.

        Returns:
            dict: Finance analytics results
        """
        url = f"https://stockpulse1.p.rapidapi.com/finance-analytics/{ticker}"
        params = kwargs
        try:
            response = requests.get(url, headers=self.api_client.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching finance analytics: {e}")
            return {}

    def get_news_results(self, ticker='ticker', **kwargs):
        """
        Get news for a given ticker.

        Args:
            ticker (str): Stock ticker symbol

        Returns:
            dict: News results
        """
        url = f"https://stockpulse1.p.rapidapi.com/news/{ticker}"
        params = kwargs
        try:
            response = requests.get(url, headers=self.api_client.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching news: {e}")
            return {}

    def get_earning_results(self, ticker='tsla', **kwargs):
        """
        Get earnings information for a given ticker.

        Args:
            ticker (str): Stock ticker symbol, default is 'tsla'.

        Returns:
            dict: Earnings results
        """
        url = f"https://stockpulse1.p.rapidapi.com/earnings/{ticker}"
        params = kwargs
        try:
            response = requests.get(url, headers=self.api_client.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching earnings: {e}")
            return {}

    def get_balance_results(self, ticker='tsla', **kwargs):
        """
        Get balance sheet information for a given ticker.

        Args:
            ticker (str): Stock ticker symbol, default is 'tsla'.

        Returns:
            dict: Balance sheet results
        """
        url = f"https://stockpulse1.p.rapidapi.com/balance-sheet/{ticker}"
        params = kwargs
        try:
            response = requests.get(url, headers=self.api_client.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching balance sheet: {e}")
            return {}
