from Calculator import Calculator,CalculError
import pytest

def test_add():
#    assert True

    calculator= Calculator()

    result = calculator.add(2,3)
    assert result == 5


def test_sub():
#    assert True

    calculator= Calculator()

    result = calculator.sub(7,3)
    assert result == 4


def test_div():
#    assert True

    calculator= Calculator()
    
    
    result = calculator.div(8,2)
    assert result == 4

def test_div_zero():
#    assert True

    calculator= Calculator()

    with pytest.raises(CalculError):
        result = calculator.div(8,0)
 #       assert result == 4
