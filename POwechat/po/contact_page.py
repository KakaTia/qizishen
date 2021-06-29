from time import sleep

from selenium.webdriver.common.by import By

from po.add_department_page import AddDepartmentPage
from po.add_member_page import AddMemberPage
from po.base_page import BasePage

# 通讯录页面
class ContactPage(BasePage):

    _ADDMEMBER = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _NAMES = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _DEPARTMENTNAME = (By.CSS_SELECTOR, 'ul[role="group"] li[role="treeitem"] .jstree-anchor')
    _PLUS = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    _AddPartment = (By.CSS_SELECTOR, '.js_create_party')
    _DEPART = (By.CSS_SELECTOR, '.js_tips')

    # 点击添加成员，进入添加成员页面
    def click_add_member(self):

        # 点击添加成员按钮
        self.wait_for_click(self._ADDMEMBER)
        return AddMemberPage(self.driver)

    # 获取成员信息进行返回,完成断言操作
    def get_member_name(self):
        # 获取后返回来有个动画操作“邀请成员”动画
        sleep(1)
        # name列表返回回来
        name_list = []
        eles = self.finds(*self._NAMES)
        for value in eles:
            name_list.append(value.get_attribute('title'))
            print(name_list)
        return name_list


    def click_add_Department(self):
        self.find_and_click(*self._PLUS)
        self.find_and_click(*self._AddPartment)
        return AddDepartmentPage(self.driver)

    # 获取信息进行返回,完成断言操作
    def get_Department_name(self):
        # 获取后返回来有个动画操作“邀请成员”动画
        sleep(2)

        Departname_list = []
        # 查到所有部门列表
        eles = self.finds(*self._DEPARTMENTNAME)

        for value in eles:
            Departname_list.append(value.text)
            print(Departname_list)
        # 返回所有部门列表
        return Departname_list

