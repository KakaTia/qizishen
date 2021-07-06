
import pytest

from PO.main_page import MainPage
import yaml
import allure

# with open('testcases/memberdata.yaml', encoding="UTF-8") as e:

with open('memberdata.yaml', encoding="UTF-8") as e:
    tatols = yaml.safe_load(e)
    tatols_info = tatols['info']
    tatols_ids = tatols['ids']

class TestDeleteMember:
    _tatols_info = tatols_info
    _tatols_ids = tatols_ids
    _PASS ="删除成功"

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass
        # self.main.driver.quit()

    @pytest.mark.parametrize('name, phone,department', _tatols_info, ids=_tatols_ids)
    @allure.feature("删除成员模块")
    def test_DeleteMember(self, name, phone, department):

        result = self.main.goto_connect_page().search_membername(name).goto_memberdelete().Delete_Member().check_deletemember(name)
        assert self._PASS in result