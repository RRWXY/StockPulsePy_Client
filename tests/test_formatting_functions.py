import pytest
from formatting_functions import (
    format_esg_score, format_stock_price, format_search_results,
    format_analytics_results, format_news_results, format_earnings_results,
    format_balance_results
)

def test_format_esg_score_valid_data():
    esg_data = {'totalEsg': {'fmt': '80'}, 'environmentScore': {'fmt': '30'}, 'socialScore': {'fmt': '30'}, 'governanceScore': {'fmt': '20'}}
    expected_output = "ESG Total Score: 80\nEnvironment Score: 30\nSocial Score: 30\nGovernance Score: 20"
    assert format_esg_score(esg_data) == expected_output

def test_format_esg_score_missing_data():
    assert format_esg_score({}) == "ESG Score data is unavailable."

def test_format_stock_price_valid_data():
    price_data = {'regularMarketPrice': {'fmt': '1000'}, 'regularMarketDayHigh': {'fmt': '1050'}, 'regularMarketDayLow': {'fmt': '950'}}
    expected_output = "Current Price: 1000\nHigh: 1050\nLow: 950"
    assert format_stock_price(price_data) == expected_output

def test_format_stock_price_missing_data():
    assert format_stock_price({}) == "Stock price data is unavailable."

def test_format_search_results_valid_data():
    data = {'quotes': [{'longname': 'Company A', 'symbol': 'CMPA'}, {'longname': 'Company B', 'symbol': 'CMPB'}]}
    expected_output = "Search Results:\n- Company A (CMPA)\n- Company B (CMPB)\n"
    assert format_search_results(data) == expected_output

def test_format_analytics_results_valid_data():
    data = {
        'currentPrice': {'fmt': '100'},
        'targetMeanPrice': {'fmt': '150'},
        'recommendationKey': 'buy'
    }
    expected_output = "Current Price: 100\nTarget Mean Price: 150\nRecommendation: buy"
    assert format_analytics_results(data) == expected_output

def test_format_analytics_results_missing_data():
    assert format_analytics_results({}) == "No analytics results found."

def test_format_news_results_valid_data():
    data = {
        '1': {'title': 'News Title 1', 'link': 'http://example.com/1'},
        '2': {'title': 'News Title 2', 'link': 'http://example.com/2'}
    }
    expected_output = "News:\n- News Title 1: http://example.com/1\n- News Title 2: http://example.com/2\n"
    assert format_news_results(data) == expected_output

def test_format_news_results_missing_data():
    assert format_news_results({}) == "No news results found."

def test_format_earnings_results_valid_data():
    data = {
        'earningsChart': {
            'quarterly': [
                {'date': '2021Q1', 'actual': {'fmt': '1.00'}, 'estimate': {'fmt': '0.90'}},
                {'date': '2021Q2', 'actual': {'fmt': '1.20'}, 'estimate': {'fmt': '1.10'}}
            ]
        }
    }
    expected_output = (
        "Earnings:\n"
        "- 2021Q1: Actual: 1.00, Estimate: 0.90\n"
        "- 2021Q2: Actual: 1.20, Estimate: 1.10\n"
    )
    assert format_earnings_results(data) == expected_output

def test_format_earnings_results_missing_data():
    assert format_earnings_results({}) == "No earnings results found."

def test_format_balance_results_valid_data():
    data = {
        'netReceivables': {'fmt': '5000'},
        'otherCurrentAssets': {'fmt': '2000'}
    }
    expected_output = "Net Receivables: 5000\nOther Current Assets: 2000"
    assert format_balance_results(data) == expected_output

def test_format_balance_results_missing_data():
    assert format_balance_results({}) == "No balance sheet results found."



# Continue with similar tests for the remaining functions
