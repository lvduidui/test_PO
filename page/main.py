from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contract import Contract
from page.login import Login

from page.register import Register


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/'

    def goto_register(self):
        self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self.driver)

    def goto_add_department(self):
        self.find(By.CSS_SELECTOR,'.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        return Contract(self.driver)
