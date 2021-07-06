from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from PO.base_page import BasePage
from PO.select_department_page import SelectDepartmentPage


class EditMemberinfoPage(BasePage):
    _NAME = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/..//*[contains(@text, "必填")]')
    _PHONE = (MobileBy.XPATH, '//*[@class="android.widget.EditText" and @text="手机号"]')
    _SELECTDEPARTMENT = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="设置部门"]')
    # _SAVE = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="保存"]')
    # _CANCELNOTICE = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="保存后自动发送邀请通知"]')
    _SAVE = "保存"
    _CANCELNOTICE = "保存后自动发送邀请通知"

    @allure.story("输入成员信息")
    def edit_memberinfo(self,name, phone):
        # 输入成员信息，点击设置部门，进入设置部门页面
        sleep(3)

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
            self.swipe_find(self._CANCELNOTICE).click()
            self.swipe_find(self._SAVE).click()
        return AddMemberPage(self.driver)