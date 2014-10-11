#!/usr/bin/env python

"""
code that tests the series funcitons defined in series.py

can be run with py.test
"""

import series as s


def test_fibs():
    """Test first several values of the s.fibonacci sequence"""
    assert s.fibonacci(0) == 0
    assert s.fibonacci(1) == 1
    assert s.fibonacci(2) == 1
    assert s.fibonacci(3) == 2
    assert s.fibonacci(4) == 3
    assert s.fibonacci(5) == 5
    assert s.fibonacci(6) == 8
    assert s.fibonacci(7) == 13


def test_lucas():
    """Test first several values of the s.lucas sequence"""
    assert s.lucas(0) == 2
    assert s.lucas(1) == 1
    assert s.lucas(2) == 3
    assert s.lucas(3) == 4
    assert s.lucas(4) == 7
    assert s.lucas(5) == 11
    assert s.lucas(6) == 18
    assert s.lucas(7) == 29
    assert s.lucas(8) == 47
    assert s.lucas(9) == 76
    assert s.lucas(10) == 123
    assert s.lucas(11) == 199
    assert s.lucas(12) == 322
    assert s.lucas(13) == 521
    assert s.lucas(14) == 843


def test_sum_series_is_fib():
    """Verify that s.sum_series(n) without optional arguments is s.fibonacci(n)"""
    for i in range(25):
        assert s.sum_series(i) == s.fibonacci(i)


def test_sum_series_is_lucas():
    """Verify that s.sum_series(n,2,1) with optional arguments 2, 1 is s.lucas(n)#"""
    for i in range(25):
        assert s.sum_series(i, 2, 1) == s.lucas(i)


def test_sum_series():
    """Verify some simple behaviors of s.sum_series(...)"""
    for i in range(25):
        assert s.sum_series(0, i, i + 1) == i
        assert s.sum_series(1, i + 1000, i) == i
        assert s.sum_series(i, 1, 1) == s.fibonacci(i + 1)
        assert s.sum_series(i, 3, 4) == s.lucas(i + 2)
