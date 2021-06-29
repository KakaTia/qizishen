from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po.base_page import BasePage


#添加部门页面
class AddDepartmentPage(BasePage):
    _Department = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input')
    _SuperiorDepartment = (By.CSS_SELECTOR, '.js_toggle_party_list')
    _FindDepartmentname = (By.CSS_SELECTOR, '.qui_dialog_body li[role="treeitem"] .jstree-anchor')
    _YesButton = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')
    # name, SuperiorDepartment
    def edit_department(self,departmentname, SuperiorDepartment):

        # 局部导入，避免循环导入，将导入放到类里面
        from po.contact_page import ContactPage

        # 新建部门页面 ，部门名称为yaml传过来的名字
        self.find(*self._Department).send_keys(departmentname)
        # 新建部门页面 ，点击所属部门
        self.wait_for_click(self._SuperiorDepartment)
        # 找到部门,找到部门点击

        self.find_and_click(By.XPATH, f"//*[contains(@class,'ww_dropdownMenu')]//*[text()='{SuperiorDepartment}']")

        #点击确定按钮
        self.find_and_click(*self._YesButton)


        return ContactPage(self.driver)