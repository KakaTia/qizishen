from time import sleep

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from PO.add_member_page import AddMemberPage
from PO.base_page import BasePage

from PO.memberinfo_page import MemberInfoPage


class ConnectPage(BasePage):
    _NAMES = (By.XPATH, "//*[@class='android.widget.TextView']")
    _ADDMEMBER=(By.XPATH, '//*[@class="android.widget.TextView" and @text="添加成员"]')
    _deletepass ="删除成功"
    _deletefail ="删除失败"
    @allure.story("点击添加成员")
    def click_add_member(self):
        self.find_and_click(*self._ADDMEMBER)
        return AddMemberPage(self.driver)

    @allure.story("搜索成员")
    def search_membername(self, name):
        with allure.step(f"搜索成员{name}，点击进入成员信息页"):
            self.swipe_find(name).click()
        return MemberInfoPage()

    def check_deletemember(self, name):
        with allure.step(f"搜索成员{name},没有找到则删除成功，否则返回删除失败"):
            try:
                sleep(3)
                self.swipe_find(name)
            except NoSuchElementException as e:
                return self._deletepass

            return self._deletefail
