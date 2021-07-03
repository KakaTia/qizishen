import allure

from PO.base_page import BasePage
from PO.connect_page import ConnectPage


class MainPage(BasePage):
    @allure.story("主页点击通讯录")
    def goto_connect_page(self):
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dqn' and @text='通讯录']").click()

        return ConnectPage(self.driver)

