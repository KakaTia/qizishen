from time import sleep

import allure
from selenium.webdriver.common.by import By

from PO.base_page import BasePage


class SelectDepartmentPage(BasePage):
    # 问题：怎么用到传过来的department把by.XPATH提取出来,赋值给_DEPARTMENTNAME？？？
    # _DEPARTMENTNAME = (By.XPATH, f'//*[@class="android.widget.TextView" and @text="{department}"]')
    _YESBUTTON = (By.ID, 'com.tencent.wework:id/fmw')


    def select_department(self, department):
        from PO.edit_memberinfo_page import EditMemberinfoPage
        # 点击销售部，进入销售部列表，再次点击销售部，点击确认按钮
        with allure.step(f"选择{department}部门，并确认"):

            self.driver.find_element(By.XPATH, f'//*[@class="android.widget.TextView" and @text="{department}"]').click()
            sleep(5)
            # 问题：传入的是销售部，第一次选择了销售部，第二次再次选择则选上了科研部，不知道为什么？
            self.driver.find_element(By.XPATH, f'//*[@class="android.widget.TextView" and @text="销售部"]').click()
            self.find(*self._YESBUTTON).click()

        return EditMemberinfoPage(self.driver)
