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


def saveData(nameF, out):
    file = io.open(nameF, 'w')
    for line in out:
        file.write(line+"\n")
    file.close()


if __name__ == '__main__':
    try:
        file = sys.argv[1]
    except IndexError:
        print "You must pass in a filename"
        sys.exit(1)
    data = io.open(file, 'r', encoding='utf-8').readlines()
    out = map(string.strip, data)
    keepGoing = True
    while keepGoing:
        try:
            outFile = raw_input("Input new filename")
            keepGoing = False
        except (EOFError, KeyboardInterrupt) as the_error:
            print the_error
            sys.exit[1]
    saveData(outFile, out)

