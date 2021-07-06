from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from PO.base_page import BasePage


class SelectDepartmentPage(BasePage):
    _YESBUTTON = (By.XPATH, '//*[contains(@text,"确定")]')


    def select_department(self, department):
        from PO.edit_memberinfo_page import EditMemberinfoPage
        # 点击销售部，进入销售部列表，再次点击销售部，点击确认按钮
        with allure.step(f"选择{department}部门，并确认"):

            # self.find_and_click(MobileBy.XPATH, f'//*[@class="android.widget.TextView" and @text="{department}"]')
            sleep(2)
            # 问题：传入的是销售部，第一次选择了销售部，第二次再次选择则选上了科研部，不知道为什么？
            self.find_and_click(MobileBy.XPATH, f'//*[contains(@text, "{department}")]/../../..//*[@class="android.widget.FrameLayout"][1]')

            self.find_and_click(*self._YESBUTTON)

        return EditMemberinfoPage(self.driver)
