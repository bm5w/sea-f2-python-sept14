#! /usr/bin/env/ python
"""Tests ack.py can use py.test"""

import unittest
from ack import ack
from numpy import matrix


def test_matrix():
    output = matrix([[1, 2, 3, 4, 5],
                     [2, 3, 4, 5, 6],
                     [3, 5, 7, 9, 11],
                     [5, 13, 29, 61, 125]   # ,
                    # [13, 65533, 2**65536-3, 2**2**65536-3, 2**2**2**65536-3]
                     ])
    for m in range(3):
        for n in range(4):
            assert ack(m, n) == output[m, n]
            # print "ack({0}, {1})".format(m, n)


def test_neg():
    assert ack(-1, 0) is None


def test_neg2():
    assert ack(2, -1) is None

if __name__ == '__main__':
    unittest.main()
