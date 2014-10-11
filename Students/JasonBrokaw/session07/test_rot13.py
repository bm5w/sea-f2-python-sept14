#!/usr/bin/env python

"""
code that tests the rot13 function defined in rot13.py

can be run with py.test
"""

import rot13 as r


def test_capitals():
    """Verify rot13 works as expected on single capital letters"""
    assert r.rot13('A') == 'N'
    assert r.rot13('Z') == 'M'


def test_lowercase():
    """Verify rot13 works as expected on single capital letters"""
    assert r.rot13('a') == 'n'
    assert r.rot13('q') == 'd'


def test_nonletters():
    """Verify that it returns non-letter characters unchanged"""
    assert r.rot13(" ?^%81") == " ?^%81"


def test_inversion_simple():
    """Verify that using the function twice returns the same string"""
    test_string = "Hello, world. Here is a test string. 1, 2; 3"
    assert test_string == r.rot13(r.rot13(test_string))
