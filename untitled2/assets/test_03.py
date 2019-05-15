# content of test_expectation.py

# coding:utf-8
# ** 作者：上海-悠悠 QQ交流群：588402570*

import pytest
@pytest.mark.parametrize("test_input,expected",
                         [("3+5",8),
                          ("4+6",10),
                          ("2+3",4),])
def test_veal(test_input,expected):
    assert eval(test_input) == expected

if __name__ == "__main__":
    pytest.main(["-s", "test_canshu1.py"])