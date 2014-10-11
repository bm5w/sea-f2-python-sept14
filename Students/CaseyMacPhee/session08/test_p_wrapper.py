import pytest

from p_wrapper import *

def test_it():
	@p_wrapper
	def take_string(str):
		return str

	c = take_string('tada')
	assert c == "<p>tada</p>"