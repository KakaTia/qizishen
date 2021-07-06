from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PO.base_page import BasePage
from PO.eidt_member_delete_page import EidtMemberDeletePage


class MemberInfoPage(BasePage):

    _Edit = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="编辑成员"]')
    _clickPoint = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text ="个人信息"]/../../../../..//android.widget.LinearLayout[2]')
    @allure.story("搜索要删除的成员")
    def goto_memberdelete(self):

        with allure.step("点击右上角竖着的三点，进入个人信息设置页"):
            self.find_and_click(*self._clickPoint)
            sleep(3)
            self.find_and_click(*self._Edit)
            # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self._Edit))

        return EidtMemberDeletePage(self.driver)