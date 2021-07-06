from appium.webdriver.common.mobileby import MobileBy
from PO.base_page import BasePage



class EidtMemberDeletePage(BasePage):
    _deletemember = "删除成员"
    _YesButton = (MobileBy.XPATH, '//*[@class="android.widget.TextView" and @text="确定"]')

    def Delete_Member(self):
        from PO.connect_page import ConnectPage
        self.swipe_find(self._deletemember).click()


        self.find_and_click(*self._YesButton)

        return ConnectPage(self.driver)