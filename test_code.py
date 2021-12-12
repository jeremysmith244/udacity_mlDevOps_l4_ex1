import numpy as np
from factorial_function import factorial

def test_factorial_1():
    assert np.math.factorial(1) == factorial(1)

def test_factorial_100():
    assert np.math.factorial(100) == factorial(100)

def test_factorial_0():
    assert np.math.factorial(0) == factorial(0)