import logging

import pytest
import yaml
import allure
from pythoncode.calculator import calculator


@allure.story("加载yaml被测数据文件内容")
def get_datas_calc():
    # with open('./datas/calc.yaml') as f:
    with open('./testing/datas/calc.yaml') as f:
        tatols = yaml.safe_load(f)
    return tatols


@allure.feature("加法和除法运算")
class TestCalculator():

    @allure.story("加法运算-整型")
    @allure.title("加法运算-整型:{a}+{b}")
    @pytest.mark.parametrize('a,b,expect', get_datas_calc()['add']['int']['datas'],
                             ids=get_datas_calc()['add']['int']['ids'])
    # @pytest.mark.add
    def test_add_int(self, get_calc_object, a, b, expect):
        if type(b) == type('s') or type(a) == type('s'):
            logging.info(f'异常情况加法运算：{a}+{b}相加 结果TypeError异常')
            with allure.step("如果相加数：int加string，处理typeError异常"):
                with pytest.raises(TypeError):
                    assert get_calc_object.add(a, b)
        else:
            logging.info(f'整数加法运算：{a}+{b}相加 结果为{expect}')
            with allure.step("除了异常情况的整数相加"):
                assert expect == get_calc_object.add(a, b)

    @allure.story("加法运算-浮点型")
    @allure.title("加法运算-浮点型:{a}+{b}")
    @pytest.mark.parametrize('a,b,expect', get_datas_calc()['add']['float']['datas'],
                             ids=get_datas_calc()['add']['float']['ids'])
    # @pytest.mark.add
    def test_add_float(self, get_calc_object, a, b, expect):
        with allure.step("相加之和，小数部分取两位"):
            logging.info(f'浮点数加法运算：{a}+{b}相加 结果为{expect}')
            assert expect == round((a + b), 2)


    @allure.story("除法运算-整型")
    @allure.title("除法运算-整型:{a}/{b}")
    @pytest.mark.parametrize('a,b,expect', get_datas_calc()['div']['int']['datas'],
                             ids=get_datas_calc()['div']['int']['ids'])
    # @pytest.mark.div
    def test_div_int(self, get_calc_object, a, b, expect):
        with allure.step("除法运算之正常整数型测试"):
            logging.info(f'整数除法运算：{a}/{b}相加 结果为{expect}')
            assert expect == get_calc_object.div(a, b)

    @allure.story("除法运算-异常处理")
    @allure.title("除法运算-异常:{a}/{b}")
    @pytest.mark.parametrize('a,b,expect', get_datas_calc()['div']['Error']['datas'],
                             ids=get_datas_calc()['div']['Error']['ids'])
    # @pytest.mark.div
    def test_div_Error(self, get_calc_object, a, b, expect):
        if type(b) == type('s') or type(a) == type('s'):
            logging.info(f'异常情况除法运算：{a}/{b}相加 结果TypeError异常')
            with allure.step("1. 处理typeError异常。"):
                with pytest.raises(TypeError):
                    assert get_calc_object.div(a, b)
        elif b == 0:
            logging.info(f'异常情况除法运算：{a}/{b}相加 结果ZeroDivisionError异常,除数不能为0')
            with allure.step("2. 除数不能为0的异常处理"):
                with pytest.raises(ZeroDivisionError):
                    assert get_calc_object.div(a, b)

        # 下面方式获取异常没有成功
        # with pytest.raises(TypeError,ZeroDivisionError):
        #     assert self.calc.div(a, b)

    @allure.story("除法运算-浮点型测试")
    @allure.title("除法运算-浮点型:{a}/{b}")
    @pytest.mark.parametrize('a,b,expect', get_datas_calc()['div']['float']['datas'],
                             ids=get_datas_calc()['div']['float']['ids'])
    # @pytest.mark.div
    def test_div_float(self, get_calc_object, a, b, expect):
        logging.info(f'浮点数除法运算：{a}/{b}相加 结果{expect}')
        with open('./testing/allure.png', 'rb') as f:
            allure.attach.file(r'./testing/allure.png', attachment_type=allure.attachment_type.PNG)
        with allure.step("除法运算之正常整数型测试"):
            assert expect == round((a / b), 2)


