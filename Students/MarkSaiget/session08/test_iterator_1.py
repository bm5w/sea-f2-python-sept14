#! /usr/bin/env python
"""Test iterator_1.py with py.test"""

import iterator_1 as it
import unittest

class iterator_1_TestCase(unittest.TestCase):
    def test_IterateMe_2(self):
        a = it.IterateMe_2(2, 20, 2)
        for x in xrange(2, 20, 2):
            assert a.next() == x

    def test_IterateMe_2_break(self):
        a = it.IterateMe_2(2, 20, 2)
        b = xrange(2, 20, 2)
        for x, y in zip(a, b):
            if y > 10: break
            assert x == y
        for x, y in zip(a, b):
            assert x == y

if __name__ == '__main__':
    unittest.main()
