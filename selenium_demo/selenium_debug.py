import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:
    def test_login(self):
        option = Options()
        option.debugger_address = "localhost:9222"

        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")


    def teardown(self):
        time.sleep(10)
        self.driver.quit()




