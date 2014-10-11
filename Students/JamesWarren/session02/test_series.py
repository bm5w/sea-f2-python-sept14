#!/usr/bin/env python

import pytest
from series import fibonacci
from series import lucas
from series import sum_series

def test_fib():
    #Tests Fibonacci function to ensure accuracy in computations
    assert fibonacci(0) == 0
    assert fibonacci(1) == 0
    assert fibonacci(5) == 3
    assert fibonacci(13) == 144

def test_lucas():
    #Tests Lucas function to ensure accuracy in computations
    assert lucas(0) == 0
    assert lucas(1) == 2
    assert lucas(5) == 7
    assert lucas(11) == 123

def test_sum():
    #Tests Sum Series function to ensure accuracy in computations
    assert sum_series(0) == 0
    assert sum_series(13) == 144
    assert sum_series(1,2,1) == 2
    assert sum_series(5,2,1) == 7
