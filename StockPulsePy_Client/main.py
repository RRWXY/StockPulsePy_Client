import pandas as pd
from .api_initialization import ApiInitialize
from .stock_data import StockData
from .analytics_data import AnalyticsData
from .formatting_functions import format_esg_score, format_stock_price, format_search_results, format_analytics_results, format_news_results, format_earnings_results, format_balance_results
import warnings
import matplotlib.pyplot as plt
import seaborn as sns


def main(companies=["tsla", "aa", "aapl"]):
    api_key = "a3456a35c9mshf4d39881959a055p15afd8jsn45e2dc9a7dd6"
    api_client = ApiInitialize(api_key)

    if api_client.validate_api():
        stock_data = StockData(api_client)
        analytics_data = AnalyticsData(api_client)

        # Example: Compare three companies
        companies = ["tsla", "aa", "aapl"] # User input can replace these
        comparison_data = []
        

        def process_esg_score(esg_data):
            lines = esg_data.split('\n')
            esg_scores = {}
            for line in lines:
                parts = line.split(': ')
                if len(parts) == 2:
                    esg_scores[parts[0]] = parts[1]
            return esg_scores
        
        def process_earnings(earnings_data):
            lines = earnings_data.split('\n')
            earnings = {"Earnings": "N/A"} 
            for line in lines:
                parts = line.split(': ')
                if len(parts) == 2:
                    key, value = parts[0], parts[1]
                    if key in earnings:
                        earnings[key] = value
            return earnings


        def process_balance_sheet(balance_sheet_data):
            lines = balance_sheet_data.split('\n')
            balance_sheet = {}
            for line in lines:
                parts = line.split(': ')
                if len(parts) == 2:
                    balance_sheet[parts[0]] = parts[1]
            return balance_sheet
        
        def process_stock_price(price_data):
            lines = price_data.split('\n')
            stock_prices = {
                "Current Price": "N/A",  
                "High": "N/A",
                "Low": "N/A"
            }
            for line in lines:
                parts = line.split(': ')
                if len(parts) == 2:
                    key, value = parts[0], parts[1]
                    if key in stock_prices:
                        stock_prices[key] = value
            return stock_prices


        
        def process_search_results(search_results_data):
            # Extract the main details from the search results string
            results = []
            if search_results_data:
                lines = search_results_data.split('\n')[1:]  # Skip the header
                for line in lines:
                    if line.strip():
                        results.append(line.strip())
            return ", ".join(results)
        
        def process_analytics(analytics_data):
            # Extract key analytics information from the string
            analytics_info = {
                "Current Price": "N/A",
                "Target Mean Price": "N/A",
                "Recommendation": "N/A"
            }
            if analytics_data:
                lines = analytics_data.split('\n')
                for line in lines:
                    if "Current Price:" in line:
                        analytics_info["Current Price"] = line.split(": ")[1]
                    elif "Target Mean Price:" in line:
                        analytics_info["Target Mean Price"] = line.split(": ")[1]
                    elif "Recommendation:" in line:
                        analytics_info["Recommendation"] = line.split(": ")[1]
            return analytics_info
        
        def process_news(news_data):
            # Summarize the news data
            news_summary = []
            if news_data:
                lines = news_data.split('\n')[1:]  # Skip the header
                for line in lines:
                    if line.strip():
                        news_summary.append(line.strip())
            return ", ".join(news_summary)

        warnings.simplefilter(action='ignore', category=FutureWarning)
        esg_comparison = pd.DataFrame(columns=["Company", "ESG Total Score", "Environment Score", "Social Score", "Governance Score"])
        stock_price_comparison = pd.DataFrame(columns=["Company", "Current Price", "High", "Low"])
        earnings_comparison = pd.DataFrame(columns=["Company", "Earnings"])
        balance_sheet_comparison = pd.DataFrame(columns=["Company", "Net Receivables", "Other Current Assets"])

        highest_stock_price = 0
        best_esg_score = 0
        best_stock_price_company = ""
        best_esg_score_company = ""
        
        for company in companies:
            # Fetch and format data
            esg_score = stock_data.get_esg_score(company)
            stock_price = stock_data.get_stock_price(company)
            search_results = analytics_data.get_search_results(company)
            analytics = analytics_data.get_analytics_results(company)
            news = analytics_data.get_news_results(company)
            earnings = analytics_data.get_earning_results(company)
            balance_sheet = analytics_data.get_balance_results(company)

            formatted_esg = format_esg_score(esg_score)
            formatted_price = format_stock_price(stock_price)
            formatted_search = format_search_results(search_results)
            formatted_analytics = format_analytics_results(analytics)
            formatted_news = format_news_results(news)
            formatted_earnings = format_earnings_results(earnings)
            formatted_balance = format_balance_results(balance_sheet)

            # Process formatted data
            processed_esg = process_esg_score(formatted_esg)
            processed_price = process_stock_price(formatted_price)
            processed_search = process_search_results(formatted_search)
            processed_analytics = process_analytics(formatted_analytics)
            processed_news = process_news(formatted_news)
            processed_earnings = process_earnings(formatted_earnings)
            processed_balance = process_balance_sheet(formatted_balance)



            # Append processed data to comparison_data
            comparison_data.append({
                "Company": company,
                "ESG Score": processed_esg,
                "Search Results": processed_search,
                "Analytics": processed_analytics,
                "News": processed_news,
                "Balance Sheet": processed_balance
            })

            esg_comparison = esg_comparison.append({
                "Company": company,
                "ESG Total Score": processed_esg.get("ESG Total Score", "N/A"),
                "Environment Score": processed_esg.get("Environment Score", "N/A"),
                "Social Score": processed_esg.get("Social Score", "N/A"),
                "Governance Score": processed_esg.get("Governance Score", "N/A"),
            }, ignore_index=True)

            stock_price_comparison = stock_price_comparison.append({
                "Company": company,
                "Current Price": processed_price.get("Current Price", "N/A"),
                "High": processed_price.get("High", "N/A"),
                "Low": processed_price.get("Low", "N/A"),
            }, ignore_index=True)

            earnings_comparison = earnings_comparison.append({
                "Company": company,
                "Earnings": processed_earnings.get("Earnings", "N/A"),
            }, ignore_index=True)

            balance_sheet_comparison = balance_sheet_comparison.append({
                "Company": company,
                "Net Receivables": processed_balance.get("Net Receivables", "N/A"),
                "Other Current Assets": processed_balance.get("Other Current Assets", "N/A"),
            }, ignore_index=True)

            # Analyze stock prices and ESG scores
            if processed_price["Current Price"] != "N/A":
                current_stock_price = float(processed_price["Current Price"].replace("$", "").replace(",", ""))
                if current_stock_price > highest_stock_price:
                    highest_stock_price = current_stock_price
                    best_stock_price_company = company

            if processed_esg["ESG Total Score"] != "N/A":
                current_esg_score = float(processed_esg["ESG Total Score"])
                if current_esg_score > best_esg_score:
                    best_esg_score = current_esg_score
                    best_esg_score_company = company

        # Convert to DataFrame and perform further analysis
        df = pd.DataFrame(comparison_data)
        df.to_csv('output.csv', index=False)

        print(df)
        print("ESG Comparison Table:")
        print(esg_comparison)
        print("\nBalance Sheet Comparison Table:")
        print(balance_sheet_comparison)
        print(f"Among the three companies you provided, the one with the best ESG performance is {best_esg_score_company} with an ESG score of {best_esg_score}. This shows that this company can more effectively manage environmental and social risks and is relatively stable.")
        
        def plot_esg_comparison(esg_comparison):
            esg_comparison_melted = esg_comparison.melt(id_vars='Company', var_name='Category', value_name='Score')
            esg_comparison_melted['Score'] = pd.to_numeric(esg_comparison_melted['Score'], errors='coerce').fillna(0)

            plt.figure(figsize=(10, 6))
            sns.lineplot(data=esg_comparison_melted, x='Category', y='Score', hue='Company', marker='o')
            plt.title("ESG Score Comparison by Category")
            plt.ylabel("Score")
            plt.xlabel("Category")
            plt.xticks(rotation=45)
            plt.legend(title='Company')
            plt.show()

        plot_esg_comparison(esg_comparison)



if __name__ == "__main__":
    main()
