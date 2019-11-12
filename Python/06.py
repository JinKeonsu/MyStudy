# www.glori.co.kr

# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "http://www.glori.co.kr/product/list.html?cate_no=141"
res = req.urlopen(url).read().decode('utf-8')
# print(res)
soup = BeautifulSoup(res, 'html.parser')

##container > div > div > div.gallery_ajax > div
#container > div > div > div.gallery_list.column5 > ul > li:nth-child(1)
items = soup.select("#contents > div.xans-element-.xans-product.xans-product-normalpackage > div.xans-element-.xans-product.xans-product-listnormal.ec-base-product > ul > li")
# print(outItems)

for item in items:
    product = item.select_one("div.info > p.name > a > span:nth-child(2)")
    print(product.text)
