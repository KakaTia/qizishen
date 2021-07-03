from time import sleep

import allure
from selenium.webdriver.common.by import By

from PO.base_page import BasePage
from PO.edit_memberinfo_page import EditMemberinfoPage


class AddMemberPage(BasePage):
    _MANUALINPUT = (By.XPATH, '//*[@class="android.widget.TextView" and @text="手动输入添加"]')
    _BACKARROW=(By.ID, 'com.tencent.wework:id/gu_')

    @allure.story("点击手动输入添加，进入成员填写页面")
    def click_manual_input(self):
        # 点击“手动输入添加”，进入输入成员信息页
        self.find(*self._MANUALINPUT).click()

        return EditMemberinfoPage(self.driver)
    @allure.story("点击左上角箭头，返回到通讯录")
    def get_membernameback(self):
        from PO.connect_page import ConnectPage
        sleep(3)
        # 点击左上角返回箭头，返回到通讯录列表
        self.find(*self._BACKARROW).click()

        return ConnectPage(self.driver)