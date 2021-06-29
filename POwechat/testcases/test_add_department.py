import pytest
import yaml

from po.main_page import MainPage

with open('departmentinfo.yaml', encoding="UTF-8") as e:
    tatols = yaml.safe_load(e)
    tatols_department_info = tatols['departmentname']
    tatols_ids = tatols['ids']


class TestAddDepart:
    _tatols_department_info = tatols_department_info
    _tatols_ids = tatols_ids

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass
        # self.main.close_driver()

    @pytest.mark.parametrize('departmentname,SuperiorDepartment', _tatols_department_info, ids=_tatols_ids)
    def test_add_member(self,departmentname, SuperiorDepartment):

        # 链式调用
        result = self.main.goto_contact_page().click_add_Department().edit_department(departmentname, SuperiorDepartment).get_Department_name()
        assert departmentname in result