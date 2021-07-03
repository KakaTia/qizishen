from time import sleep

import allure
from selenium.webdriver.common.by import By

from PO.add_member_page import AddMemberPage
from PO.base_page import BasePage


class ConnectPage(BasePage):
    _NAMES = (By.XPATH, "//*[@class='android.widget.TextView']")
    _ADDMEMBER=(By.XPATH, '//*[@class="android.widget.TextView" and @text="添加成员"]')
    @allure.story("点击添加成员")
    def click_add_member(self):
        self.find(*self._ADDMEMBER).click()
        return AddMemberPage(self.driver)

    @allure.story("为了断言得到包含成员名字的列表")
    def get_membername(self):
        sleep(3)
        name_list = []
        eles = self.finds(*self._NAMES)
        for value in eles:
            name_list.append(value.get_attribute('text'))
        print(name_list)
        return name_list
