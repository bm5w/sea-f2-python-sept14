import pytest
from series import lucas

def test_luc():
	assert lucas(3) == 3
	assert lucas(4) == 4
	assert lucas(5) == 7
