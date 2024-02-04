import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to fetch stock news from Moneycontrol
def fetch_moneycontrol_news(stock_symbol):
    base_url = f'https://www.moneycontrol.com/news/business/companies/{stock_symbol}.html'
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_elements = soup.find_all('div', class_='fltlft news-con')
        news_list = []

        for news_element in news_elements:
            title = news_element.find('h2').text.strip()
            link = news_element.find('a')['href']
            news_list.append({'title': title, 'link': link})

        return news_list

    else:
        st.error(f"Error fetching data from Moneycontrol. Status code: {response.status_code}")
        return None

# Streamlit app
def main():
    st.title("Moneycontrol Stock News Scraper")

    # Sidebar for user input
    stock_symbol = st.sidebar.text_input("Enter Stock Symbol", value='tatasteel')
    search_button = st.sidebar.button("Search")

    if search_button:
        # Fetch and display stock news
        news_data = fetch_moneycontrol_news(stock_symbol)

        if news_data:
            st.header(f"Latest Stock News for {stock_symbol.upper()}")
            for news_item in news_data:
                st.write(f"- [{news_item['title']}]({news_item['link']})")

if __name__ == "__main__":
    main()
