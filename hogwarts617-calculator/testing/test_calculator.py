import pytest
import yaml
import allure

from pythoncode.calculator import calculator


def get_adddatas_calc():

    # When you use the right mouse button to run the code, this code will succeed
    # with open('./datas/calc.yaml') as f:

    # When you use Terminal to run the code, this code will succeed
    with open('./testing/datas/calc.yaml') as f:

        tatols = yaml.safe_load(f)
    return (tatols['adddatas'], tatols['addids'])


def get_divdatas_calc():

    # with open("./datas/calc.yaml") as f2:
    with open("./testing/datas/calc.yaml") as f2:

        tatolsdiv = yaml.safe_load(f2)
    return (tatolsdiv['divdatas'], tatolsdiv['divids'])


@allure.feature("加法和除法测试")
class TestCalculator:

    def setup(self):
        self.calc = calculator()
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @allure.story("加法运算测试")
    @pytest.mark.parametrize('a,b,addexpect', get_adddatas_calc()[0], ids=get_adddatas_calc()[1])
    @pytest.mark.add
    def test_add(self, a, b, addexpect):
        if b == 's':
            with pytest.raises(TypeError) as e1:
                self.calc.add(a, b)

            assert e1.type == TypeError

            assert f"unsupported operand type(s) for +: 'int' and 'str'" in e1.value.args[0]
        else:
            assert addexpect == self.calc.add(a, b)

    @allure.story("除法运算测试")
    @pytest.mark.parametrize('c,d,divexpect', get_divdatas_calc()[0], ids=get_divdatas_calc()[1])
    @pytest.mark.div
    def test_div(self, c, d, divexpect):
        if d == 's':
            with pytest.raises(TypeError) as e:
                self.calc.div(c, d)

            assert e.type == TypeError

            assert f"unsupported operand type(s) for /: 'int' and 'str'" in e.value.args[0]
        else:

            try:
                res = self.calc.div(c, d)
            except Exception as e:
                print("发生异常，异常信息{}，进行异常断言".format(e))
                assert str(e) == 'division by zero'

            else:
                assert divexpect == res
