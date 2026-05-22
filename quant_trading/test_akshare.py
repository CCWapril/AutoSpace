import akshare as ak
try:
    stock_list = ak.stock_zh_a_spot_em()
    print(f"Successfully fetched {len(stock_list)} stocks")
    print(stock_list.head())
except Exception as e:
    print(f"Error: {e}")
