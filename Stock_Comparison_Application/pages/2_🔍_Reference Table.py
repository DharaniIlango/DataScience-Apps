import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Reference Table - Stock Price Comparison App",page_icon='🔍', layout="wide")

# Function to load the Excel file from the app directory
@st.cache_data
def load_excel(file_path):
    return pd.read_excel(file_path)

# Function to paginate through the DataFrame
def paginate_dataframe(df, page_size, page_num):
    # Calculate start and end index of rows to display
    start_idx = page_num * page_size
    end_idx = min(start_idx + page_size, len(df))
    return df.iloc[start_idx:end_idx]

# Streamlit app
# Display reference table for user reference
st.title("🔍 Reference Table for Stock Tickers")
st.markdown("Enter the correct stock tickers in the Stock Comparison tab to compare their prices. Example tickers: 'AAPL' for Apple, 'AMZN' for Amazon, 'GOOG' for Google.")


# Define the path to the dataset in your app directory
file_path = "Stock_Ticker.xlsx"  # Replace with the actual filename

try:
    # Load the Excel file into a DataFrame
    df = load_excel(file_path)

    # Determine the total number of rows and pages
    total_rows = len(df)
    page_size = 100  # Number of rows per page
    total_pages = (total_rows // page_size) + (total_rows % page_size > 0)

    # Select the page to view
    page_num = st.number_input("Page Number", min_value=1, max_value=total_pages, step=1, value=1) - 1

    # Display the current page of data
    st.write(f"Displaying rows {(page_num * page_size) + 1} to {min((page_num + 1) * page_size, total_rows)} out of {total_rows}")
    
    # Paginate the data and reset the index to start from 1
    paginated_data = paginate_dataframe(df, page_size, page_num)
    paginated_data.index = range((page_num * page_size) + 1, (page_num * page_size) + len(paginated_data) + 1)  # Reset index starting from 1

    # Increase the size of the displayed table by using `st.dataframe` with `use_container_width=True`
    st.dataframe(paginated_data, use_container_width=True, height=800)  # Adjust height here

    # Option to download the entire dataset as CSV
    csv = df.to_csv(index=False)
    st.download_button("Download Full Dataset as CSV", data=csv, file_name="Stock_Ticker_Table.csv", mime="text/csv")

except FileNotFoundError:
    st.error(f"File '{file_path}' not found. Please ensure the file is correctly placed in the app directory.")
