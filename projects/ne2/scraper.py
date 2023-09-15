from bs4 import BeautifulSoup
import requests as r

url = 'https://www.flipkart.com/search?q=smart%20watch&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
try:
    response = r.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print('sucess')
except Exception as e:
    print(e)

target = soup.find('div', class_ = '_1YokD2 _3Mn1Gg')
if target:
    print("yes")
else:
    print('no')

products = target.find_all('div', class_ = '_1AtVbE col-12-12')
if products:
    print("yes product found!")
    total = len(products)
    print (f'{total} products are there.')
else:
    print("No Product Found!!")

# for item in products:
#     try: title = item.find