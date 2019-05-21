# Naver cafe 자동 출첵 쓰기 실습

import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class NaverCafeAutoAttend:
    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/jinkeonsu/Project/Python_project/inflearn/section3/webdriver/chromedriver')
        self.driver = webdriver.Chrome('/Users/jinkeonsu/Project/Python_project/inflearn/section3/webdriver/chromedriver')
        self.driver.implicitly_wait(5)

    def writeAttend(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('thebrave')
        self.driver.find_element_by_name('pw').send_keys('do2019!')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get('https://cafe.naver.com/mcbugi')
        self.driver.implicitly_wait(30)
        self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=16914752&search.menuid=6')
        self.driver.implicitly_wait(30)
        # self.driver.switch_to_frame('cafe_main')
        # self.driver.find_element_by_id('cmtinput').send_keys('Good evening~~~')
        # self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click()
        time.sleep(30000)

    def __del__(self):
        self.driver.quit()

if __name__ == '__main__':
    a = NaverCafeAutoAttend()
    start_time = time.time()
    a.writeAttend()
    print(" Total %s seconds" % (time.time()-start_time))
    # del a

#근데.. 아래 오류가 나면서.. 안되네..
# 드라이버로 로그인할때 캡차 문자까지 필요하게 네이버에서 변경한듯하다..
# 지금보니까.. 강의 하단에 관련 공지가 있었구나!!!
# 일단은 내용 파악하는 수준에서 마무리. 실습은 다른 사이트를 해보거나, 나중에 하거나...


# Traceback (most recent call last):
#   File "/Users/jinkeonsu/Project/Python_project/inflearn/section3/3-7-1.py", line 41, in <module>
#     a.writeAttend()
#   File "/Users/jinkeonsu/Project/Python_project/inflearn/section3/3-7-1.py", line 30, in writeAttend
#     self.driver.switch_to_frame('cafe_main')
#   File "/anaconda/envs/section3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 789, in switch_to_frame
#     self._switch_to.frame(frame_reference)
#   File "/anaconda/envs/section3/lib/python3.5/site-packages/selenium/webdriver/remote/switch_to.py", line 89, in frame
#     self._driver.execute(Command.SWITCH_TO_FRAME, {'id': frame_reference})
#   File "/anaconda/envs/section3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
#     self.error_handler.check_response(response)
#   File "/anaconda/envs/section3/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 241, in check_response
#     raise exception_class(message, screen, stacktrace, alert_text)
# selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: None
# Message: unexpected alert open: {Alert text : 멤버에게 공개된 게시판입니다.}
#   (Session info: chrome=74.0.3729.157)
#   (Driver info: chromedriver=74.0.3729.6 (255758eccf3d244491b8a1317aa76e1ce10d57e9-refs/branch-heads/3729@{#29}),platform=Mac OS X 10.14.4 x86_64)
