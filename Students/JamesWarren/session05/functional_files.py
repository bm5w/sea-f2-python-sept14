#!/usr/bin/env python
import io
import sys
import string

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

    source_in = io.open(file_in, mode='r').readlines()
    file_out = io.open(file_out, mode='w')

    ### Map() Method
    #write_out = map(string.strip, source_in)
    #for line in write_out:
    #    file_out.write(line+'\n')
    ###

    ### List Comprehension Method
    write_out = [line.strip()+'\n' for line in source_in]
    file_out.writelines(write_out)
    ###

    print "** PROCESS COMPLETE **"

elif conf.lower() == "n":
    print
    print "Exiting..."
    print
    print "----------"
    sys.exit()
else:
    print "Invalid entry. Now exiting..."
