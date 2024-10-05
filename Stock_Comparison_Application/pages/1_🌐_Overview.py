import streamlit as st

# Set page title
st.set_page_config(page_title="Stock Price Comparison App",page_icon='🌐', layout="wide")

# Add a title and description
st.title(" 📈 Stock Price Comparison Application")
st.header("Overview")
   
st.markdown("""
### Introduction
The **Stock Price Comparison Application** is an intuitive web-based tool designed for users to easily compare the stock performance of multiple companies over various time frames. Built using **Streamlit** and integrated with the **Yahoo Finance API**, the app provides real-time stock data, allowing for dynamic visualization of stock price trends. The interface is simple yet powerful, enabling both casual users and investors to track and analyze market trends in a highly interactive manner.
""")

# Key Features Section
st.markdown("### Key Features")
st.markdown("""
1. **User-Friendly Sidebar Navigation**:
   - The application features a **sidebar menu** for easy navigation, allowing users to switch between two main views:
     - **Company Reference Table**: A quick reference guide that maps company names to their stock tickers.
     - **Stock Comparison Tool**: An interactive feature that allows users to select multiple companies and compare their stock performance.

2. **Company Ticker Reference Table**:
   - A concise and handy reference table that provides the stock ticker symbols for different companies.
   - Users can easily search for company tickers to better understand and identify the stock they are interested in comparing.

3. **Stock Comparison Tool**:
   - Users can select multiple companies from a predefined list and **compare their stock prices** side-by-side on a dynamic line graph.
   - The comparison is based on stock performance over a selected period, providing insights into how different companies are performing relative to each other.

4. **Adjustable Time Frame Selection**:
   - The stock comparison tool includes a **slider** that allows users to **customize the time frame** for analysis, ranging from **1 month to 12 months**.
   - This feature enables users to explore both short-term fluctuations and long-term trends in stock prices.

5. **Interactive Line Chart Visualization**:
   - The stock data is plotted using a **Plotly line chart**, offering a clear and interactive visualization of the price movements over time.
   - Each company's stock is displayed with a unique color for easy differentiation, and users can hover over the graph to view detailed data points.
""")

# Technical Implementation Section
st.markdown("### Technical Implementation")
st.markdown("""
- **Streamlit**: The app leverages the simplicity and flexibility of Streamlit for building and deploying the web application.
- **Yahoo Finance API**: The stock price data is fetched in real-time through the Yahoo Finance API, ensuring the information is up-to-date and accurate.
- **Plotly**: The app uses Plotly to create dynamic and visually appealing line charts, enabling interactive data exploration.
- **Pandas**: The Pandas library is used to handle, transform, and manipulate the stock data, allowing for seamless data management and analysis.
""")

# User Experience Section
st.markdown("### User Experience")
st.markdown("""
1. **Clean and Simple Interface**:
   - The sidebar provides a clear and intuitive navigation system, allowing users to effortlessly switch between viewing the reference table and the stock comparison tool.
   
2. **Real-Time Stock Data**:
   - Users can compare the real-time stock performance of multiple companies and gain insights into their trends over different time frames.

3. **Customizable Time Frames**:
   - The time period for stock comparison can be adjusted easily using the slider, enabling users to choose between short-term (e.g., 1 month) and long-term (e.g., 12 months) trends.

4. **Visually Engaging Charts**:
   - The dynamic line chart makes it easy to visualize stock price movements, with color-coded lines representing different companies. The interactive nature of the chart allows users to explore specific data points and trends in detail.
""")

# Use Cases Section
st.markdown("### Use Cases")
st.markdown("""
- **Investors**: The tool is ideal for investors looking to compare the stock performance of multiple companies to make informed investment decisions.
- **Market Analysts**: Analysts can use the app to study and identify trends, patterns, and market behaviors over various time periods.
- **Casual Users**: Individuals who want to keep track of company stocks and observe market trends can use the app for quick insights.
""")

# Conclusion Section
st.markdown("### Conclusion")
st.markdown("""
The **Stock Price Comparison Application** provides a seamless and efficient way for users to track and compare stock performance across multiple companies over customizable time frames. Whether for investment analysis or general market observation, this tool combines real-time data, an easy-to-navigate interface, and dynamic visualization to deliver meaningful insights into stock trends. With just a few clicks, users can explore the financial market and make informed decisions based on data-driven analysis.
""")
