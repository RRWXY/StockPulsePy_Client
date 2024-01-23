import pytest
from unittest.mock import Mock, patch
from stock_data import StockData

class TestStockData:
    @pytest.fixture
    def api_client_mock(self):
        # Create a mock for the API client
        mock_client = Mock()
        mock_client.headers = {'Authorization': 'Bearer testtoken'}
        return mock_client

    @patch('stock_data.requests.get')
    def test_get_esg_score(self, mock_get, api_client_mock):
        # Mock successful API response
        mock_get.return_value = Mock(status_code=200, json=lambda: {'score': 85})
        stock_data = StockData(api_client_mock)

        # Call the method
        result = stock_data.get_esg_score('AAPL')

        # Assert the result is as expected
        assert result == {'score': 85}

