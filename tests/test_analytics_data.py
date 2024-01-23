import pytest
from unittest.mock import Mock, patch
from analytics_data import AnalyticsData

class TestAnalyticsData:
    @pytest.fixture
    def api_client_mock(self):
        # Create a mock for the API client
        mock_client = Mock()
        mock_client.headers = {'Authorization': 'Bearer testtoken'}
        return mock_client

    @patch('analytics_data.requests.get')
    def test_get_search_results(self, mock_get, api_client_mock):
        # Mock successful API response
        mock_response = {'result': 'success'}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        analytics = AnalyticsData(api_client_mock)

        result = analytics.get_search_results('test_query')

        assert result == mock_response

    @patch('analytics_data.requests.get')
    def test_get_analytics_results(self, mock_get, api_client_mock):
        # Mock successful API response
        mock_response = {'result': 'success'}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        analytics = AnalyticsData(api_client_mock)

        result = analytics.get_analytics_results('test_query')

        assert result == mock_response   

    @patch('analytics_data.requests.get')
    def test_get_news_results(self, mock_get, api_client_mock):
        # Mock successful API response
        mock_response = {'result': 'success'}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        analytics = AnalyticsData(api_client_mock)

        result = analytics.get_news_results('test_query')

        assert result == mock_response 

    @patch('analytics_data.requests.get')
    def test_get_earning_results(self, mock_get, api_client_mock):
        # Mock successful API response
        mock_response = {'result': 'success'}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        analytics = AnalyticsData(api_client_mock)

        result = analytics.get_earning_results('test_query')

        assert result == mock_response 

    @patch('analytics_data.requests.get')
    def test_get_balance_results(self, mock_get, api_client_mock):
        # Mock successful API response
        mock_response = {'result': 'success'}
        mock_get.return_value = Mock(status_code=200, json=lambda: mock_response)
        analytics = AnalyticsData(api_client_mock)

        result = analytics.get_balance_results('test_query')

        assert result == mock_response 


