# Stock Price Comparison App

📈 This application allows users to compare the stock prices of multiple companies over a selected time period. Users can input stock ticker symbols and visualize their price trends dynamically.

# Live Preview
The Project is live, checkout the following URL -> [Stock-Comparison-Application](https://stock-comparison-application.streamlit.app/Overview)
## Features

- **User Input for Tickers**: Users can enter multiple stock ticker symbols separated by commas (e.g., `AAPL, AMZN, GOOG`).
- **Dynamic Time Period Selection**: A slider allows users to select the time frame for the stock price comparison, with options ranging from 1 month to 1 year.
- **Interactive Charting**: Stock price data is visualized using Plotly, providing an interactive line chart that shows price trends for each stock over the selected time frame.
- **Real-time Data Fetching**: Stock data is fetched using the Yahoo Finance API (`yfinance`), ensuring that users have access to the latest market data.

## Application Structure

- **fetch_stock_data(tickers, period)**: 
  - Fetches historical stock price data for the specified tickers and time period using the Yahoo Finance API.
  - **Parameters**:
    - `tickers`: A list of stock ticker symbols (e.g., `['AAPL', 'AMZN']`).
    - `period`: The time period for historical data (e.g., `1y`, `6mo`, `3mo`, `1mo`).

- **plot_stock_data(stock_data)**:
  - Plots the stock price data on an interactive line chart.
  - **Parameters**:
    - `stock_data`: A DataFrame containing stock prices indexed by date.

## Application Data

- **Data Source**: The application utilizes the Yahoo Finance API to fetch historical stock price data.
- **Data Fields**: The main data fields used in the application include:
  - **Date**: The date of the stock price entry.
  - **Close**: The closing price of the stock for the given date.

## Usage

1. Open the application in your web browser.
2. Enter the stock ticker symbols you wish to compare.
3. Adjust the time period using the slider.
4. Observe the dynamically generated chart displaying stock price comparisons.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any changes or enhancements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.