#! /usr/bin/env python
"""Functional Files"""
"""Write a program that takes a filename and "cleans" the file be removing all
the leading and trailing whitespace from each line.
Read in the original file and write out a new one, either creating a new file
or overwriting the existing one.
Give your user the option of which to perform.
Use map() to do the work.
"""
import sys
import io
import string


def cleanup(x):
    """given line input, cleanup whitespace on leading and trailing ends."""
    return x.strip()


# def readData(name):
#     file = open(name, 'r')
#     lines = file.read()
#     file.close()
#     return lines


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "format: inFile outFile"
        sys.exit(1)
    else:
        file = sys.argv[1]
        try:
            outFile = sys.argv[2]
        except IndexError:
            outFile = file
    data = io.open(file, 'r', encoding='utf-8').readlines()
    out = map(string.strip, data)
    keepGoing = True
    io.open(outFile, 'w').writelines(out)

