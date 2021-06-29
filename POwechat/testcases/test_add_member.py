import pytest
import yaml

from po.main_page import MainPage



with open('memberinfo.yaml', encoding="UTF-8") as e:
     tatols = yaml.safe_load(e)
     tatols_info = tatols['info']
     tatols_ids = tatols['ids']


class TestAddMember:
    _tatols_info = tatols_info
    _tatols_ids = tatols_ids

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        # self.main.close_driver()
        pass

    @pytest.mark.parametrize('name,englishname,acctid,phone,mail,expect', _tatols_info, ids=_tatols_ids)
    def test_add_member(self,name, englishname, acctid, phone, mail, expect):

        # 链式调用
        result = self.main.goto_contact_page().click_add_member().edit_member(name, englishname, acctid, phone, mail, expect).get_member_name()
        assert "彦程" in result