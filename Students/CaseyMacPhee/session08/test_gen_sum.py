import pytest
from generators import gen_sum

def test_sum():
	s = gen_sum()
	assert s.next() == 0
	assert s.next() == 1
	assert s.next() == 3
	assert s.next() == 6
	assert s.next() == 10
	assert s.next() == 15
	assert s.next() == 21