import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import streamlit as st

@st.cache_data
def calculate_indicators(df):
    """
    Calculate technical indicators for the dataframe.
    """
    # Create a copy to avoid modifying the original if cached
    df = df.copy()
    # SMA
    df['sma_5'] = df['close'].rolling(window=5).mean()
    df['sma_10'] = df['close'].rolling(window=10).mean()
    df['sma_20'] = df['close'].rolling(window=20).mean()
    
    # RSI
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))
    
    # MACD
    exp1 = df['close'].ewm(span=12, adjust=False).mean()
    exp2 = df['close'].ewm(span=26, adjust=False).mean()
    df['macd'] = exp1 - exp2
    df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()
    
    # Volatility (Bollinger Bands)
    df['std'] = df['close'].rolling(window=20).std()
    df['upper_band'] = df['sma_20'] + (df['std'] * 2)
    df['lower_band'] = df['sma_20'] - (df['std'] * 2)
    
    # Target: 1 if next day's close > current day's close, else 0
    df['target'] = (df['close'].shift(-1) > df['close']).astype(int)
    
    return df.dropna()

@st.cache_resource
def train_model(df):
    """
    Train a simple Random Forest model to predict price movement.
    """
    features = ['sma_5', 'sma_10', 'sma_20', 'rsi', 'macd', 'macd_signal', 'upper_band', 'lower_band']
    X = df[features]
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, predictions))
    
    return model

if __name__ == "__main__":
    from data_loader import get_stock_data
    df = get_stock_data("sh600519", start_date="20200101", end_date="20231231")
    if df is not None:
        df = calculate_indicators(df)
        model = train_model(df)
        print("Model trained successfully")
    else:
        print("Failed to get data for training")
