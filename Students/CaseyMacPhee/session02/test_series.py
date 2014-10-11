import pytest

from series import sum_series

def test_sum():
	assert sum_series(3) == 2
	assert sum_series(12) == 144
	assert sum_series(3, 3, 5) == 3