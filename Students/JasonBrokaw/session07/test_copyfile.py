#!/usr/bin/env python

"""
code that tests the copyfile function defined in copyfile.py

can be run with py.test
"""

import pytest, io

import copyfile as c


def test_arguments():
    """Verify that it raises an exception if wrong arguments are passed (for command line usage)"""
    with pytest.raises(TypeError):
        c.copyfile()

    with pytest.raises(TypeError):
        c.copyfile("a")


def test_bad_name():
    """Verify that it raises and exception if the input file doesn't exist"""
    with pytest.raises(IOError) as erinfo:
        c.copyfile("adflkjaer", "anything.txt")
        assert "No such file" in erinfo.value


def test_functionality():
    """Try copying a little file"""
    infile = io.open("test_in.txt", "w")
    infile.write(u"Some text\n with some stuff in!!")
    infile.close()
    c.copyfile("test_in.txt", "test_out.txt")
    assert io.open("test_out.txt", "r").read() == u"Some text\n with some stuff in!!"
