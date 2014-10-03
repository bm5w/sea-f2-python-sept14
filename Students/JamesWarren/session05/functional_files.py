#!/usr/bin/env python
import io
import sys

file_in = sys.argv[1]
file_out = sys.argv[2]

print "-----"
print
print "FILE IN -- ", file_in
print "FILE OUT -- ", file_out
print 
print "-----"
print

conf = raw_input("Are you sure you want to overwrite %s? [y/n] > " % file_out)

if conf.lower() == "y":

    fi = io.open(file_in, mode='r')
    source = fi.read()
    fi.close()

    #fo = io.open(file_out, mode='w')

elif conf.lower() == "n":
    print
    print "Exiting..."
    print "----------"
    sys.exit()
else:
    pass
