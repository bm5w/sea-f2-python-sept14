#!/usr/bin/env python
"""
Perform Ackermann function.
http://en.wikipedia.org/wiki/Ackermann_function
A(m, n) =
    n+1   if  m = 0
    A(m-1, 1)  if  m > 0 and n = 0
    A(m-1, A(m, n-1))  if m > 0 and n > 0
Return none when inputs are less than zero.
"""


def ack(m, n):
    """Perform Ackermann function."""
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

if __name__ == '__main__':
    """Test m and n values from 0 to 4, given values in wikipedia table.
    # Only run when module is run (ie from command line)
    Cannot test m = 4 values as they exceed recursion limit of python.
    """
    from numpy import matrix
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
    assert ack(-1, 0) is None
    assert ack(2, -1) is None
    print u"All Tests Pass"
