import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# class TestHogwards():
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         #窗口最大化
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(3)
#     def teardown(self):
#         time.sleep(10)
#         self.driver.quit()
#
#     def test_hogwards(self):
#         self.driver.get('http://www.testerhome.com')
#         self.driver.find_element_by_link_text("社团").click()
#         self.driver.find_element_by_link_text("霍格沃兹测试学院").click()



class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        #隐式等待
        self.driver.implicitly_wait(3)
    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="归入各种类别的所有主题"]').click()
        #显式等待，必须得带参数，
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]')) >=1
        # WebDriverWait(self.driver,10).until(wait)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题""]').click()


