import streamlit as st
import requests

# Function to fetch news data based on the provided API endpoint
def fetch_news(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data from {endpoint}. Status code: {response.status_code}")
        return None

# Streamlit app
def main():
    st.title("Stock News App")

    # Sidebar for user input
    stock_symbol = st.sidebar.text_input("Enter Stock Symbol", value='AAPL')
    search_button = st.sidebar.button("Search")

    # Fetch and display latest news
    latest_news_endpoint = f"https://mc-api-j0rn.onrender.com/api/latest_news?symbol={stock_symbol}"
    latest_news_data = fetch_news(latest_news_endpoint)

    if latest_news_data:
        st.header(f"Latest News for {stock_symbol}")
        for news_item in latest_news_data:
            st.write(f"- {news_item.get('title', 'N/A')}")

    # Display business news
    business_news_endpoint = "https://mc-api-j0rn.onrender.com/api/business_news"
    business_news_data = fetch_news(business_news_endpoint)

    if business_news_data:
        st.header("Business News")
        for news_item in business_news_data:
            st.write(f"- {news_item.get('title', 'N/A')}")

    # Display a list of stocks
    stock_list_endpoint = "https://mc-api-j0rn.onrender.com/api/list"
    stock_list_data = fetch_news(stock_list_endpoint)

    if stock_list_data:
        st.sidebar.header("Stock List")
        for stock_item in stock_list_data:
            symbol = stock_item.get('symbol', 'N/A')
            name = stock_item.get('name', 'N/A')
            st.sidebar.write(f"- {symbol} ({name})")

if __name__ == "__main__":
    main()
