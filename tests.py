from main import add
from main import soustraire
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-2, 3) == 1
def test_soustraire():
    assert soustraire(6, 3) == 3
    assert soustraire(0, 0) == 0
    assert soustraire(5, 3) == 2