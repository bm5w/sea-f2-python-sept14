#!/usr/bin/env python

import pytest
from rot13 import rot13

def test_rot13_1():
    assert rot13("This is a test!") == "Guvf vf n grfg!"

def test_rot13_2():
    assert rot13("The quick brown fox jumps over the lazy dog.") == \
    "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."

def test_rot13_3():
    assert rot13("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.") == \
    "The quick brown fox jumps over the lazy dog."