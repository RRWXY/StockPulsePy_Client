import requests
import os
import pandas as pd

class ApiInitialize:
    def __init__(self, api_key):
        """
        Initialize the ApiInitialize class with the API key.

        Args:
            api_key (str): API key string.
        """
        self.api_key = api_key
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "stockpulse1.p.rapidapi.com"
        }

    def validate_api(self):
        """
        Validate the API key's validity.

        Returns:
            bool: True if the API key is valid, False otherwise.
        """
        test_url = "https://rapidapi.com"
        try:
            response = requests.get(test_url, headers=self.headers)
            response.raise_for_status()
            return True
        except requests.RequestException:
            return False