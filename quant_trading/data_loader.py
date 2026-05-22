import akshare as ak
import pandas as pd
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

# Inject retry strategy
session = requests.Session()
retry_strategy = Retry(
    total=5,
    backoff_factor=2,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)
ak._requests_session = session

def get_stock_data(symbol, period="daily", start_date="20230101", end_date="20231231"):
    """
    Fetch historical stock data using AkShare (Sina source).
    """
    try:
        # Sina source usually requires sh/sz prefix
        if not (symbol.startswith("sh") or symbol.startswith("sz")):
            if symbol.startswith("6"):
                symbol = "sh" + symbol
            else:
                symbol = "sz" + symbol
        
        df = ak.stock_zh_a_daily(symbol=symbol, start_date=start_date, end_date=end_date, adjust="qfq")
        if df is None or df.empty:
            print(f"No data found for {symbol}")
            return None
        
        # Standardizing column names for Sina data
        # Sina columns: date, open, high, low, close, volume, amount, outstanding_share, turnover
        mapping = {
            'date': 'date', 'open': 'open', 'high': 'high', 'low': 'low', 
            'close': 'close', 'volume': 'volume', 'amount': 'amount', 
            'turnover': 'turnover'
        }
        df.rename(columns=mapping, inplace=True)
        
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
            df.set_index('date', inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def get_market_news(date_str=None):
    """
    Fetch high-level market news from CCTV.
    """
    if date_str is None:
        date_str = time.strftime("%Y%m%d")
    try:
        df = ak.news_cctv(date=date_str)
        return df
    except Exception as e:
        print(f"Error fetching market news: {e}")
        return None

def get_stock_news(symbol):
    """
    Fetch news for a specific stock.
    """
    try:
        # stock_news_em returns recent news for the market or specific stocks if filtered
        # For simplicity, we get general stock news
        df = ak.stock_news_em(symbol=symbol)
        return df
    except Exception as e:
        print(f"Error fetching stock news: {e}")
        return None

def get_hot_stocks():
    """
    Fetch current hot stock rankings.
    """
    try:
        df = ak.stock_hot_rank_em()
        return df
    except Exception as e:
        print(f"Error fetching hot stocks: {e}")
        return None

if __name__ == "__main__":
    # Test with Kweichow Moutai (600519)
    test_symbol = "sh600519"
    data = get_stock_data(test_symbol)
    if data is not None:
        print(f"Successfully fetched {len(data)} rows for {test_symbol}")
        print(data.head())
    else:
        print("Failed to fetch data.")
