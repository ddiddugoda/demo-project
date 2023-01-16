# Basic test function
import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


# Test function verifies an exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)
