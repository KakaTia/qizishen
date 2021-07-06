import allure
from selenium.webdriver.common.by import By

from PO.base_page import BasePage
from PO.connect_page import ConnectPage


class MainPage(BasePage):
    _CONNECTNAME=(By.XPATH,"//*[@class='android.widget.TextView' and @text='通讯录']")

    @allure.story("主页点击通讯录")
    def goto_connect_page(self):
        self.find_and_click(*self._CONNECTNAME)

        return ConnectPage(self.driver)

