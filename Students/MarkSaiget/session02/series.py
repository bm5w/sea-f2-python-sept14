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


def sum_series(n, a=0, b=1):
    """Perform sum series to find nth value in series.
    Parameter n is the number in the sum series.
    Optional parameter a is the first value in the series.
    Optional parameter b is the second value in the series.
    Without optional parameters, sum_series is a fibonacci sequence.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return sum(n-2) + sum(n-1)
print "lucas(8) = ", lucas(8)
