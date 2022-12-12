import pytest
from pythonplayground.example import add_one


def test_add_one():
    i = 3
    j = add_one(i)
    assert j == (i+1)

def test_add_two():
    i = 3
    j = add_one(i)
    k = add_one(j)
    assert k == (i+2)



if __name__ == "__main__":  # pragma: no cover
    pytest.main()