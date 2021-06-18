import pytest
import yaml

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


class TestCalculator:

    def setup(self):
        self.calc = calculator()
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,addexpect', get_adddatas_calc()[0], ids=get_adddatas_calc()[1])
    @pytest.mark.add
    def test_add(self, a, b, addexpect):
        # calc = calculator()
        assert addexpect == self.calc.add(a, b)
        # assert 2 == self.calc.add(1, 1)

    @pytest.mark.parametrize('c,d,divexpect', get_divdatas_calc()[0], ids=get_divdatas_calc()[1])
    @pytest.mark.div
    def test_div(self, c, d, divexpect):
        # calc = calculator()
        # assert 1 == self.calc.div(1, 1)
        assert divexpect == self.calc.div(c, d)
