#!/usr/env/python

import sys

if __name__ == '__main__':
	filename = raw_input("What's the name of the file? (full path)\n: ")

else:
	filename = sys.argv[1]

copyordel = raw_input("Type 'c' to conserve the old file and copy, or 'ow' to overwrite\n: ")
while copyordel != 'c' and copyordel != 'ow':
	copyordel = raw_input("Type 'c' to conserve the old file and copy, or 'ow' to overwrite\n: ")


if copyordel == 'c':
	newfilename = filename + '_copy'
	newfile = open(newfilename, 'w')


try:
	thefile = open(filename, 'rw+')
except:
	print "Please provide a valid file path"

try:
	while True:
		line = thefile.next()
		line = line.strip()
		if copyordel == 'c':
			newfile.write(line + '\n')
		elif copyordel == 'ow':
			thefile.write(line + '\n')
except:
	print "Finished"
thefile.close()

if copyordel == 'c':
	newfile.close()







