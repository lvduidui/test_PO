from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Contract(BasePage):
    #添加部门
    def add_department(self):
        self.find(By.XPATH,'//*[@class="inputDlg_item"]/input').send_keys('王者荣耀')
        self.find(By.CSS_SELECTOR,'.qui_dialog_body.ww_dialog_body [id="1688850183092817_anchor"]').click()
        self.find(By.CSS_SELECTOR, '.qui_btn ww_btn ww_btn_Blue').click()

        return Contract(self.driver)

    #获取部门列表
    def get_department_list(self):
        department_list = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-anchor')
        departments_list = []
        for department in department_list:
            departments_list.append(department)

        return departments_list

