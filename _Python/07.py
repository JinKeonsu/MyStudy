# b2pet

from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 2. 옵션을 줘서 웹 드라이버 생성
chrome_options = Options()
chrome_options.add_argument("--headless")   #CLI
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/jinkeonsu/Project/Python_project/inflearn/section3/webdriver/chromedriver')

# driver.set_window_size(1920,1280)
# driver.implicitly_wait(3)

driver.get('http://www.2bpet.co.kr/product/list_best.asp?type=new')
time.sleep(3)
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
items = soup.select("#container > div > div > div.gallery_ajax > div > ul > li")

for item in items:
    name = item.select_one("div.con > div.txt > div.tit > a").string
    print(name)

# driver.quit()
print(' complete')
