import pytest

from generators import gen_fib

def test_gen_fib():
	y = gen_fib()

	assert y.next() == 0
	assert y.next() == 1
	assert y.next() == 1
	assert y.next() == 2
	assert y.next() == 3
	assert y.next() == 5
	assert y.next() == 8
	assert y.next() == 13
	assert y.next() == 21
	


