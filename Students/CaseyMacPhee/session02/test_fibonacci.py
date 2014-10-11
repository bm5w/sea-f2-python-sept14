import pytest
from series import fibonacci
def test_fib():
	assert fibonacci(3) == 2
	assert fibonacci(4) == 3
	assert fibonacci(5) == 5
