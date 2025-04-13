from src.add8 import add8

def test_suma_5_3():
    assert add8(5, 3) == [0, 0, 0, 1, 0, 0, 0, 0, 0]

def test_suma_max_1():
    assert add8(255, 1) == [0, 0, 0, 0, 0, 0, 0, 0, 1]

def test_suma_0_0():
    assert add8(0, 0) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
