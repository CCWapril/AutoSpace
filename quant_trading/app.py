import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data_loader import get_stock_data, get_market_news, get_stock_news, get_hot_stocks
from strategy import calculate_indicators, train_model
from backtester import run_backtest
import datetime

st.set_page_config(page_title="A股实时量化交易助手", layout="wide")

# Initialize session state for simulated trading
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {"cash": 100000.0, "stocks": {}}

st.title("📈 A股实时量化交易助手")

# Sidebar
st.sidebar.header("参数设置")
stock_code = st.sidebar.text_input("请输入股票代码 (如: 600519)", "600519")
start_date = st.sidebar.date_input("开始日期", datetime.date(2023, 1, 1))
end_date = st.sidebar.date_input("结束日期", datetime.date.today())

# Tabs for different sections
tab_analysis, tab_market, tab_portfolio = st.tabs(["🔍 个股分析", "🌍 市场资讯", "💰 我的持仓"])

with tab_analysis:
    if st.sidebar.button("开始分析"):
        with st.spinner("正在获取数据并训练模型..."):
            # Format dates for AkShare
            start_str = start_date.strftime("%Y%m%d")
            end_str = end_date.strftime("%Y%m%d")
            
            # 1. Fetch Data
            df = get_stock_data(stock_code, start_date=start_str, end_date=end_str)
            
            if df is not None and not df.empty:
                # 2. Feature Engineering
                df = calculate_indicators(df)
                
                # 3. Train Model
                model = train_model(df)
                
                # 4. Generate Signals
                features = ['sma_5', 'sma_10', 'sma_20', 'rsi', 'macd', 'macd_signal', 'upper_band', 'lower_band']
                df['signal'] = model.predict(df[features])
                
                # Display results
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.subheader(f"{stock_code} 价格与信号展示")
                    fig = go.Figure()
                    fig.add_trace(go.Candlestick(x=df.index,
                                                open=df['open'],
                                                high=df['high'],
                                                low=df['low'],
                                                close=df['close'],
                                                name="价格"))
                    
                    # Add Buy Signals
                    buy_signals = df[df['signal'] == 1]
                    fig.add_trace(go.Scatter(x=buy_signals.index, y=buy_signals['close'],
                                            mode='markers', marker=dict(symbol='triangle-up', size=10, color='green'),
                                            name='买入信号'))
                    
                    # Add Sell Signals
                    sell_signals = df[df['signal'] == 0]
                    fig.add_trace(go.Scatter(x=sell_signals.index, y=sell_signals['close'],
                                            mode='markers', marker=dict(symbol='triangle-down', size=10, color='red'),
                                            name='卖出信号'))
                    
                    fig.update_layout(xaxis_rangeslider_visible=False, height=600)
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    st.subheader("回测报告")
                    metrics = run_backtest(df)
                    st.metric("最终资产", f"{metrics['final_value']:,.2f}")
                    st.metric("总收益率", f"{metrics['total_return']:.2f}%")
                    st.metric("夏普比率", f"{metrics['sharpe_ratio']:.2f}")
                    st.metric("最大回撤", f"{metrics['max_drawdown']:.2f}%")
                    
                    st.divider()
                    st.subheader("模拟交易")
                    current_price = df['close'].iloc[-1]
                    st.write(f"当前价格: {current_price:.2f}")
                    amount = st.number_input("购买数量", min_value=100, step=100, value=100)
                    if st.button("模拟买入"):
                        cost = current_price * amount
                        if st.session_state.portfolio["cash"] >= cost:
                            st.session_state.portfolio["cash"] -= cost
                            st.session_state.portfolio["stocks"][stock_code] = st.session_state.portfolio["stocks"].get(stock_code, 0) + amount
                            st.success(f"成功买入 {amount} 股 {stock_code}")
                        else:
                            st.error("余额不足")

                st.subheader("个股相关新闻")
                stock_news = get_stock_news(stock_code)
                if stock_news is not None and not stock_news.empty:
                    for idx, row in stock_news.head(5).iterrows():
                        st.write(f"**{row['发布时间']}**: {row['新闻标题']}")
                        st.write(f"[阅读全文]({row['新闻链接']})")
                
                st.subheader("数据预览")
                st.dataframe(df.tail(10))
                
            else:
                st.error("未能获取到数据，请检查股票代码或日期设置。")
    else:
        st.info("请在左侧侧边栏输入股票代码并点击'开始分析'。")

with tab_market:
    col1, col2 = st.columns(2)
    
    with col2:
        st.subheader("📰 今日焦点新闻 (CCTV)")
        news = get_market_news()
        if news is not None:
            for idx, row in news.head(10).iterrows():
                with st.expander(row['title']):
                    st.write(row['content'])
        else:
            st.write("无法获取市场新闻。")
            
    with col1:
        st.subheader("🔥 实时热门股票 (推荐)")
        hot_stocks = get_hot_stocks()
        if hot_stocks is not None:
            st.dataframe(hot_stocks.head(10))
        else:
            st.write("无法获取热门股票。")

with tab_portfolio:
    st.subheader("我的模拟账户")
    st.metric("可用资金", f"{st.session_state.portfolio['cash']:,.2f}")
    if st.session_state.portfolio["stocks"]:
        portfolio_df = pd.DataFrame([
            {"代码": k, "持仓数量": v} for k, v in st.session_state.portfolio["stocks"].items()
        ])
        st.dataframe(portfolio_df)
    else:
        st.write("当前无持仓。")
