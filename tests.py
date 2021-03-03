import pytest

a = 1.4
b = {
    'item1': 1,
    'item2': 2
}

#test 1 for float
def test_a1():
    assert a == 1.4

#test 2 for float
def test_a2():
    assert a > 2

#test 3 for float
@pytest.mark.parametrize("test_input, expected", [(1.2 + 0.2, a), (1 + 2, a)])
def test_a3(test_input, expected):
    assert test_input == expected

#test 1 for dict
def test_b1():
    assert b['item1'] == b['item2']

#test 2 for dict
def test_b2():
    assert b['item1'] < b['item2']

#test 3 for dict
@pytest.mark.parametrize("test_input, expected", [("1 + 0", b['item1']), ("1 + 2", b['item2'])])
def test_b3(test_input, expected):
    assert eval(test_input) == expected