def ack(m, n):
    """Perform Ackermann function."""
    # function is not defined for input values less than 0
    # Check inputs are greater than zero.
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

if __name__ == '__main__':
    """Test m and n values from 0 to 4, in ackermann function."""
    # Only run when module is run (ie from command line)
    from numpy import matrix
    output = matrix([[1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 5, 7, 9, 11],
        [5, 13, 29, 61, 125]#,
        #[13, 65533, 2**65536-3, 2**2**65536-3, 2**2**2**65536-3]
    ])
    print 'made it here'

    for m in range(3):
        for n in range(4):
            assert ack(m, n) == output[m, n]
            print "ack({0}, {1})".format(m, n)
    print "All Tests Pass"
