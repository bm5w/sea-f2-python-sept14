#!/usr/bin/env python

"""
code that tests the lambda_magic function defined in lambda_magic.py

can be run with py.test
"""

import lambda_magic as l


def test_callability():
    """Test that the list contains functions"""
    the_list = l.function_builder(4)
    for func in the_list:
        assert hasattr(func, '__call__')


def test__values():
    """Test some values to verify expected behavior"""
    the_list = l.function_builder(4)
    assert the_list[0](2) == 2
    assert the_list[1](2) == 3
    for i in xrange(4):
        for j in xrange(4):
            assert the_list[i](j) == i + j

