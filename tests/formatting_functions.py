import requests
import os
import pandas as pd

def format_esg_score(esg_data):
    if not esg_data or 'totalEsg' not in esg_data:
        return "ESG Score data is unavailable."

    esg_score = esg_data['totalEsg'].get('fmt', 'N/A')
    environment_score = esg_data['environmentScore'].get('fmt', 'N/A')
    social_score = esg_data['socialScore'].get('fmt', 'N/A')
    governance_score = esg_data['governanceScore'].get('fmt', 'N/A')

    formatted_output = (
        f"ESG Total Score: {esg_score}\n"
        f"Environment Score: {environment_score}\n"
        f"Social Score: {social_score}\n"
        f"Governance Score: {governance_score}"
    )


    return formatted_output

def format_stock_price(price_data):
    if not price_data:
        return "Stock price data is unavailable."

    price = price_data.get('regularMarketPrice', {}).get('fmt', 'N/A')
    high = price_data.get('regularMarketDayHigh', {}).get('fmt', 'N/A')
    low = price_data.get('regularMarketDayLow', {}).get('fmt', 'N/A')

    formatted_output = (
        f"Current Price: {price}\n"
        f"High: {high}\n"
        f"Low: {low}"
    )

    return formatted_output

def format_search_results(data):
    if not data or 'quotes' not in data:
        return "No search results found."

    formatted_output = "Search Results:\n"
    for item in data['quotes']:
        formatted_output += f"- {item.get('longname', 'N/A')} ({item.get('symbol', 'N/A')})\n"

    return formatted_output

def format_analytics_results(data):
    if not data:
        return "No analytics results found."

    current_price = data.get('currentPrice', {}).get('fmt', 'N/A')
    target_mean_price = data.get('targetMeanPrice', {}).get('fmt', 'N/A')
    recommendation = data.get('recommendationKey', 'N/A')

    formatted_output = (
        f"Current Price: {current_price}\n"
        f"Target Mean Price: {target_mean_price}\n"
        f"Recommendation: {recommendation}"
    )

    return formatted_output

def format_news_results(data):
    if not data:
        return "No news results found."

    formatted_output = "News:\n"
    for key, news_item in data.items():
        if isinstance(news_item, dict):
            title = news_item.get('title', 'N/A')
            link = news_item.get('link', 'N/A')
            formatted_output += f"- {title}: {link}\n"

    return formatted_output

def format_earnings_results(data):
    if not data or 'earningsChart' not in data:
        return "No earnings results found."

    formatted_output = "Earnings:\n"
    for quarter in data['earningsChart']['quarterly']:
        date = quarter.get('date', 'N/A')
        actual = quarter.get('actual', {}).get('fmt', 'N/A')
        estimate = quarter.get('estimate', {}).get('fmt', 'N/A')
        formatted_output += f"- {date}: Actual: {actual}, Estimate: {estimate}\n"

    return formatted_output

def format_balance_results(data):
    if not data:
        return "No balance sheet results found."

    net_receivables = data.get('netReceivables', {}).get('fmt', 'N/A')
    other_assets = data.get('otherCurrentAssets', {}).get('fmt', 'N/A')

    formatted_output = (
        f"Net Receivables: {net_receivables}\n"
        f"Other Current Assets: {other_assets}"
    )

    return formatted_output