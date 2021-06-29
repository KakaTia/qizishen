import logging
from selenium.webdriver.common.by import By
from po.base_page import BasePage


# 添加成员页面
class AddMemberPage(BasePage):

    _NAME = (By.ID, 'username')
    _ENGLISHNAME = (By.ID, 'memberAdd_english_name')
    _ACCTID = (By.ID, 'memberAdd_acctid')
    _PHONE = (By.ID, 'memberAdd_phone')
    _MAIL = (By.ID, 'memberAdd_mail')

    _SAVE = (By.CSS_SELECTOR, '.js_btn_save')

    # list = []
    # list=get_memberinfo()

    def edit_member(self, name, englishname, acctid, phone, mail, expect):

        # 添加成员信息，保存后，返回通讯录页面

        # 局部导入，避免循环导入，将导入放到类里面
        from po.contact_page import ContactPage

        # 添加成员信息
        logging.info(f"添加成员信息")
        self.find(*self._NAME).send_keys(name)
        self.find(*self._ENGLISHNAME).send_keys(englishname)
        self.find(*self._ACCTID).send_keys(acctid)
        self.find(*self._PHONE).send_keys(phone)
        self.find(*self._MAIL).send_keys(mail)

        # 保存成员信息
        self.find_and_click(*self._SAVE)
        return ContactPage(self.driver)


