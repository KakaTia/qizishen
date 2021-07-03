import allure
from selenium.webdriver.common.by import By

from PO.base_page import BasePage
from PO.select_department_page import SelectDepartmentPage


class EditMemberinfoPage(BasePage):
    _NAME = (By.XPATH, '//*[@resource-id="com.tencent.wework:id/au0" and @text="必填"]')
    _PHONE = (By.XPATH, '//*[@class="android.widget.EditText" and @text="手机号"]')
    _SELECTDEPARTMENT = (By.XPATH, '//*[@class="android.widget.TextView" and @text="设置部门"]')
    _SAVE = (By.ID, 'com.tencent.wework:id/gur')
    @allure.story("输入成员信息")
    def edit_memberinfo(self,name, phone):
        # 输入成员信息，点击设置部门，进入设置部门页面
        with allure.step("输入成员名字"):
            self.find(*self._NAME).send_keys(name)
        with allure.step("输入成员手机号"):
            self.find(*self._PHONE).send_keys(phone)
        with allure.step("点击设置部门"):
            self.find(*self._SELECTDEPARTMENT).click()

        return SelectDepartmentPage(self.driver)

    def get_department(self):
        from PO.add_member_page import AddMemberPage
        with allure.step("点击保存，返回添加成员页面"):
            self.find(*self._SAVE).click()
        return AddMemberPage(self.driver)