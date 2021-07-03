
from appium import webdriver
import pytest

from PO.main_page import MainPage
import yaml
import allure

with open('testcases/memberdata.yaml', encoding="UTF-8") as e:
    tatols = yaml.safe_load(e)
    tatols_info = tatols['info']
    tatols_ids = tatols['ids']


class TestAddMember:
    _tatols_info = tatols_info
    _tatols_ids = tatols_ids
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass
        # self.main.driver.quit()

    @pytest.mark.parametrize('name, phone,department', _tatols_info, ids=_tatols_ids)
    @allure.feature("添加成员模块")
    def test_AddMember(self, name, phone, department):

        result = self.main.goto_connect_page().click_add_member().click_manual_input().edit_memberinfo(name, phone).select_department(department).get_department().get_membernameback().get_membername()
        assert name in result

