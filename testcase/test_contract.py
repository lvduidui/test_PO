import time

from selenium.webdriver.common.by import By

from page.main import Main


class TestContract:
    def setup(self):
        self.main = Main()
        self.main.driver.get('https://work.weixin.qq.com')
        self.main.driver.maximize_window()
        self.main.goto_login()
        time.sleep(8)
        self.main.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(2)
        self.main.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        time.sleep(2)

    def teardown(self):
        pass

    def test_add_department(self):
        result = self.main.goto_add_department().add_department().get_department_list()
        assert '王者荣耀' in result

