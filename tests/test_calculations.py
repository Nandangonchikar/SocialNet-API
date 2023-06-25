from app.calculations import add
import pytest

@pytest.mark.parametrize("test_input1,test_input2,expected",[
    (5,12,17),
    (7,14,21),
    (0,7,8),
    (-1,6,5)
])

def test_add(test_input1,test_input2,expected):
    print("Running test for add()...")
    assert add(test_input1,test_input2)==expected

