def test_sample():
    assert 1 + 1 == 2
from main import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
def test_add_negative_numbers():
    from main import add_numbers
    assert add_numbers(-5, -3) == -8
    assert add_numbers(10, -10) == 0
