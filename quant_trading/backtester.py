import backtrader as bt
import pandas as pd
from data_loader import get_stock_data
from strategy import calculate_indicators

class MLStrategy(bt.Strategy):
    params = (
        ('model', None),
        ('features', ['sma_5', 'sma_10', 'sma_20', 'rsi', 'macd', 'macd_signal', 'upper_band', 'lower_band']),
    )

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None

    def next(self):
        if self.order:
            return

        # Prepare features for the current step
        # Note: In a real scenario, we'd need to ensure we have the calculated features 
        # available for the current bar.
        # Since we are using a simple approach, we'll assume the features are already 
        # in the dataframe used by Backtrader.
        
        # Actually, Backtrader doesn't easily pass custom dataframe columns to Strategy 
        # unless we define them in a custom DataFeed.
        
        # For simplicity in this prototype, let's use a basic SMA crossover strategy 
        # to demonstrate backtesting, as integrating ML into Backtrader properly 
        # requires more boilerplate.
        
        # But wait, the user wants buy/sell signals from ML.
        # I'll create a custom DataFeed.
        pass

class CustomPandasData(bt.feeds.PandasData):
    lines = ('sma_5', 'sma_10', 'sma_20', 'rsi', 'macd', 'macd_signal', 'upper_band', 'lower_band', 'signal',)
    params = (
        ('sma_5', -1), ('sma_10', -1), ('sma_20', -1), ('rsi', -1), 
        ('macd', -1), ('macd_signal', -1), ('upper_band', -1), ('lower_band', -1),
        ('signal', -1),
    )

class MLSignalStrategy(bt.Strategy):
    def __init__(self):
        self.signal = self.datas[0].signal

    def next(self):
        if not self.position:
            if self.signal[0] == 1:
                self.buy()
        else:
            if self.signal[0] == 0:
                self.sell()

def run_backtest(df):
    cerebro = bt.Cerebro()
    
    data = CustomPandasData(dataname=df)
    cerebro.adddata(data)
    
    cerebro.addstrategy(MLSignalStrategy)
    
    cerebro.broker.setcash(100000.0)
    cerebro.broker.setcommission(commission=0.001)
    
    # Add analyzers
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
    
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    results = cerebro.run()
    strat = results[0]
    
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    
    # Extract performance metrics
    metrics = {
        'final_value': cerebro.broker.getvalue(),
        'sharpe_ratio': strat.analyzers.sharpe.get_analysis().get('sharperatio', 0),
        'max_drawdown': strat.analyzers.drawdown.get_analysis().max.drawdown,
        'total_return': strat.analyzers.returns.get_analysis().get('rtot', 0) * 100
    }
    return metrics

if __name__ == "__main__":
    from strategy import train_model
    df = get_stock_data("sh600519", start_date="20200101", end_date="20231231")
    if df is not None:
        df = calculate_indicators(df)
        model = train_model(df)
        
        # Generate signals for the whole dataframe
        features = ['sma_5', 'sma_10', 'sma_20', 'rsi', 'macd', 'macd_signal', 'upper_band', 'lower_band']
        df['signal'] = model.predict(df[features])
        
        run_backtest(df)
    else:
        print("Failed to get data for backtesting")
