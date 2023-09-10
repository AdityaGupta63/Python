import requests
from bs4 import BeautifulSoup


url = 'https://www.amazon.in/Apple-Cellular-Rugged-Titanium-Orange/dp/B0BDKGNMJQ?ref_=ast_sto_dp&th=1'

Header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

link = requests.get(url, headers=Header)

soup = BeautifulSoup(link.content, 'html.parser')
print(soup)
