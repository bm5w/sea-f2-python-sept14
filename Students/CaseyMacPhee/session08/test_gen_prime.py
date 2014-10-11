import pytest
from generators import gen_prime

def test_prime():
	j = gen_prime()
	assert j.next() == 2
	assert j.next() == 3
	assert j.next() == 5
	assert j.next() == 7
	assert j.next() == 11
	assert j.next() == 13
	assert j.next() == 17
	assert j.next() == 19
	assert j.next() == 23
	assert j.next() == 29
	assert j.next() == 31