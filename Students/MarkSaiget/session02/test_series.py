#! /usr/bin/env python
"""Test for series.py, which can utilize py.test"""

fib_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
lucas_values = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]

from series import fibonacci, lucas, sum_series


def test_fib():
    
    # Check fibonacci sequence values are as expected
    for i in range(1, len(fib_values)+1):
        assert fib_values[i-1] == fibonacci(i)


def test_lucas():
    # Check lucas sequence values are as expected
    for i in range(1, len(lucas_values)+1):
        assert lucas_values[i-1] == lucas(i)


def test_sum():
    # Check sum_series function, test list using default (fibonacci) values
    for i in range(1, len(fib_values)+1):
        assert sum_series(i) == fib_values[i-1]


def test_sum_2_1():
    # Check sum_series function, test list using 2,1 (sum_series) values
    for i in range(1, len(lucas_values)+1):
        assert sum_series(i, 2, 1) == lucas_values[i-1]


def test_neg():
    # Check functions with negative n values.
    assert sum_series(-1, 2, 1) is None
    assert fibonacci(-4) is None
    assert lucas(0) is None

