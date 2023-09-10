import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.amazon.in/Apple-iPhone-13-Mini-512GB/dp/B09G997HJP/?_encoding=UTF8&pd_rd_w=oSi5X&content-id=amzn1.sym.e5c03be3-10ba-4bc8-b9be-6fcea12320ed%3Aamzn1.symc.adba8a53-36db-43df-a081-77d28e1b71e6&pf_rd_p=e5c03be3-10ba-4bc8-b9be-6fcea12320ed&pf_rd_r=94M7V2D4X2BXEZFXDS2M&pd_rd_wg=3WRAM&pd_rd_r=9d7bb830-91e8-43d3-89fd-7e908857b451&ref_=pd_gw_ci_mcx_mr_hp_atf_m')

soup = BeautifulSoup(url.content, 'html.parser')
print(soup.find(id='corePriceDisplay_desktop_feature_div'))