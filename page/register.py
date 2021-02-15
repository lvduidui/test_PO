from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, 'corp_name').send_keys('hello')
        return True
