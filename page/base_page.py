import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)
        self.driver.implicitly_wait(3)

    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开文件
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()



    def find(self, by, locator):
        return self.driver.find_element(by, locator)
