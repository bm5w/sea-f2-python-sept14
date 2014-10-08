import pytest

from generators import gen_doubler

def test_doubler():
	s = gen_doubler()

	assert s.next() == 1
	assert s.next() == 2
	assert s.next() == 4
	assert s.next() == 8
	assert s.next() == 16
	assert s.next() == 32
	assert s.next() == 64
	assert s.next() == 128
	assert s.next() == 256