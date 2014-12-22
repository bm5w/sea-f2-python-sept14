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


if __name__ == "__main__":
    """Perform block of tests using assert statements to check functions."""
    fib_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    lucas_values = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]

    # Check fibonacci sequence values are as expected
    for i in range(1, len(fib_values)+1):
        assert fib_values(i) == fibonacci(i)

    # Check lucas sequence values are as expected
    for i in range(1, len(lucas_values)+1):
        assert lucas_values(i) == lucas(i)

    # Check sum_series function, test list using default (fibonacci) values
    for i in range(len(fib_values)):
        assert sum_series(i) == fib_values(i-1)

    # Check sum_series function, test list using 2,1 (sum_series) values
    for i in range(len(lucas_values)):
        assert sum_series(i, 2, 1) == fib_values(i-1)
    print "All tests pass"
