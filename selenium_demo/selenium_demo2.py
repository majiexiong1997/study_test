from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()


    def test_html(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('百度贴吧')
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="s_tab"]//b').click()
        elements = self.driver.find_elements(By.XPATH,'//*[@id="s_tab"]//a')

        for element in elements:
            pass
        #     self.driver.find_element(By.XPATH,element).click()
        # pass



