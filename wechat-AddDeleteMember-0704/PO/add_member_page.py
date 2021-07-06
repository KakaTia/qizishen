from os.path import exists
from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from PO.base_page import BasePage
from PO.edit_memberinfo_page import EditMemberinfoPage


class AddMemberPage(BasePage):
    _MANUALINPUT = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="手动输入添加"]')
    _IntegrityInput = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="完整输入"]')
    _fastInput = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="快速输入"]')
    _GETTOAST = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    @allure.story("点击手动输入添加，进入成员填写页面")
    def click_manual_input(self):
        # 点击“手动输入添加”，进入输入成员信息页
        self.find(*self._MANUALINPUT).click()
        sleep(3)
        # 完整输入 被显示在界面上则点击
        try:
            self.find(*self._IntegrityInput)
        except NoSuchElementException as e:
            return EditMemberinfoPage(self.driver)
        self.find(*self._IntegrityInput).click()
        return EditMemberinfoPage(self.driver)

    @allure.story("添加成功")
    def get_result(self):
        result = self.find(*self._GETTOAST).get_attribute('text')
        self.back()
        return result
