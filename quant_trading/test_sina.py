import akshare as ak
try:
    df = ak.stock_zh_a_daily(symbol="sh600000", start_date="20230101", end_date="20231231", adjust="qfq")
    print(f"Success: {len(df)} rows")
    print(df.head())
except Exception as e:
    print(f"Error: {e}")
