import logging

import allure
from api.contact import Contactpage


@allure.feature("通讯录模块")
class TestContact:
    def setup_class(self):
        self.contactpage = Contactpage()

    @allure.story("创建成员")
    def test_create(self):
        r = self.contactpage.create()
        print(r.json())
        assert r.json().get("errcode") == 0

    @allure.story("更改成员信息")
    def test_modify(self):
        r = self.contactpage.modify()
        print(r.json())
        assert r.json().get("errcode") == 0

    @allure.story("获取成员信息")
    def test_get(self):
        r = self.contactpage.get()
        print(r.json())
        assert r.json().get("errcode") == 0

    @allure.story("删除成员")
    def test_delete(self):
        r = self.contactpage.delete()
        print(r.json())
        assert r.json().get("errcode") == 0
