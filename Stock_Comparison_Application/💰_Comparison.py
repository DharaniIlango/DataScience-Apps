import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Stock Price Comparison", page_icon="📊", layout="wide")

# Stock data fetcher function
@st.cache_data
def fetch_stock_data(tickers, period="1y"):
    stock_data = {}
    for ticker in tickers:
        stock_data[ticker] = yf.Ticker(ticker).history(period=period)['Close']
    return pd.DataFrame(stock_data)

# Stock data plotter function
def plot_stock_data(stock_data):
    stock_data.reset_index(inplace=True)
    stock_data = stock_data.melt(id_vars='Date', var_name='Stock', value_name='Price')
    fig = px.line(stock_data, x='Date', y='Price', color='Stock', title='Stock Price Comparison')
    st.plotly_chart(fig)

# Display stock comparison UI
st.title("📈 Stock Price Comparison")
st.markdown("""
Compare the stock prices of multiple companies over a selected time period. 
Enter the ticker symbols for the stocks you want to compare, and adjust the time range dynamically to visualize stock trends.
""")
    
# Text input for users to enter stock tickers
user_tickers = st.text_input("Enter stock tickers (separate by commas)", value="AAPL, AMZN, GOOG")

# Split the user input into a list of ticker symbols
if user_tickers:
    ticker_symbols = [ticker.strip().upper() for ticker in user_tickers.split(",")]

    # Slider to adjust the time period dynamically
    st.markdown("### Select Time Frame:")
    period_options = {"1 Year": "1y", "6 Months": "6mo", "3 Months": "3mo", "1 Month": "1mo"}
    selected_period_label = st.slider("Time Period", min_value=1, max_value=12, value=12, step=1, format="%d Months")
        
    # Map slider value to corresponding period
    if selected_period_label == 12:
        period = "1y"
    elif selected_period_label >= 6:
        period = "6mo"
    elif selected_period_label >= 3:
        period = "3mo"
    else:
        period = "1mo"

    # Fetch and plot the stock data
    stock_data = fetch_stock_data(ticker_symbols, period)
    st.subheader(f"Stock Price Comparison for the Last {selected_period_label} Months")
    plot_stock_data(stock_data)