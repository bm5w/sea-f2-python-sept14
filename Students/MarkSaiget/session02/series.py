"""
Fibonacci Series
Lucas Numbers
Sum Series
"""


def fibonacci(n):
    """Perform fibonacci series to find nth value in series.
    Parameter n is the number in the fibonacci series.
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """Perform lucas series to find nth value in series.
    Parameter n is the number in the lucas series.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)
print "lucas(8) = ", lucas(8)