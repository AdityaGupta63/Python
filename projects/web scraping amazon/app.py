import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(
    page_title='Amazon Web Scraping'
)

st.title('Amazon Web Scraping Project !')
st.subheader('A program that extracts product information, reviews and rating from Amazon.com .')


url = 'https://www.amazon.in/Apple-Cellular-Rugged-Titanium-Orange/dp/B0BDKGNMJQ?ref_=ast_sto_dp&th=1'

Header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

link = requests.get(url, headers=Header)

soup = BeautifulSoup(link.content, 'html.parser')

st.title(soup.find_all(id='productTitle')).title