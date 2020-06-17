import json
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # https://work.weixin.qq.com/wework_admin/frame
        self.driver.implicitly_wait(10)
    # def test_cookie(self):
    #     time.sleep(15)
    #     cookies = self.driver.get_cookies()
    #     with open('cookie.json','w') as f:
    #         json.dump(cookies,f)
    def teardown(self):
        self.driver.quit()
    def test_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        #//*[@id="menu_index"]   首页按钮
        while True:
            #显式等待首页按钮并持续刷新，当返回的ele不为空时退出循环
            self.driver.refresh()
            menu_index = WebDriverWait(self.driver,10).\
            until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="menu_index"]')))
            if menu_index is not None:
                break
        self.driver.find_element(By.XPATH,'//*[@class="index_service_cnt js_service_list"]/a[2]').click()
        self.driver.find_element(By.XPATH,'//*[@id="js_upload_file_input"]')\
            .send_keys(r'C:\Users\Administrator\PycharmProjects\study_test\selenium_demo\test.xlsx')
        #检测文件是否放入放入
        WebDriverWait(self.driver,10).\
            until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="upload_file_name"]')))
        text_name = self.driver.find_element(By.XPATH,'//*[@id="upload_file_name"]').text
        assert text_name == 'test.xlsx'




