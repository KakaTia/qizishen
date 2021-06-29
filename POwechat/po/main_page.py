from selenium.webdriver.common.by import By

from po.base_page import BasePage
from po.contact_page import ContactPage

# 主页
class MainPage(BasePage):
    #避免页面用到很多次这个元素，下划线_为私有变量，推荐的大家约定
    _CONTACT=(By.ID, "menu_contacts")
    # 跳转到通讯录页面
    def goto_contact_page(self):
        # *为解码，是解元组，把(By.ID, "menu_contacts")元组拆开By.ID和"menu_contacts"
        self.find_and_click(*self._CONTACT)

        return ContactPage(self.driver)
