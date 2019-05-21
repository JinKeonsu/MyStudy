# Selenium & chromedriver 실습
# selenium-python


import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 1. 기본 웹 드라이버 생성
driver = webdriver.Chrome('/Users/jinkeonsu/Project/Python_project/inflearn/section3/webdriver/chromedriver')

# 2. 옵션을 줘서 웹 드라이버 생성
# chrome_options = Options()
# chrome_options.add_argument("--headless")   #CLI
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/jinkeonsu/Project/Python_project/inflearn/section3/webdriver/chromedriver')

# screenshot
# driver.get('https://google.com')
# driver.save_screenshot('/Users/jinkeonsu/Project/Python_project/inflearn/section3/webdriver/capture1.png')
#
# driver.get('https://www.daum.net')
# driver.save_screenshot('/Users/jinkeonsu/Project/Python_project/inflearn/section3/webdriver/capture2.png')

# inflearn 사이트에 아이디, 패스워드 입력 후 로그인 해보기 #
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get('https://www.wishket.com/accounts/login/')
time.sleep(3)
driver.implicitly_wait(3)

driver.find_element_by_name('identification').send_keys('thebrave')
driver.implicitly_wait(1)
driver.find_element_by_name('password').send_keys('c2wk')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/div/button').click()

driver.quit()
print('capture complete')
