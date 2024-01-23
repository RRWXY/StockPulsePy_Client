import pytest
from unittest.mock import Mock, patch
from api_initialization import ApiInitialize

class TestApiInitialize:
    def test_init(self):
        # Testing the initialization process
        api_key = 'testapikey'
        api_init = ApiInitialize(api_key)

        assert api_init.api_key == api_key
        assert api_init.headers == {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "stockpulse1.p.rapidapi.com"
        }

    @patch('api_initialization.requests.get')
    def test_validate_api(self, mock_get):
        # Mocking successful API validation
        mock_get.return_value = Mock(status_code=200)
        api_key = 'validapikey'
        api_init = ApiInitialize(api_key)

        # Assuming validate_api returns True on successful validation
        assert api_init.validate_api() == True

