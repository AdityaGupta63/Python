import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(
    page_title='Flipkart Web Scraping'
)
url = 'https://www.snapdeal.com/search?keyword=smart%20watch&sort=rlvncy'
Header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
link = requests.get(url, headers=Header)

st.title('Amazon Web Scraping Project !')
st.subheader('A program that extracts product information, reviews and rating from Amazon.com .')



soup = BeautifulSoup(link.content, 'html.parser')

target = soup.find('div', class_ = 'product-row js-product-list centerCardAfterLoadWidgets dp-click-widgets')
# if target:
#     st.markdown('found')
# else:
#     st.markdown('not found')

product = target.find_all('div', class_ = 'js-section clearfix dp-widget dp-fired')
st.markdown(product)
