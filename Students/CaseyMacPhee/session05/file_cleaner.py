#!/usr/env/python

import sys

if __name__ == '__main__':
	filename = sys.argv[1]
	
else:
	filename = raw_input("What's the name of the file? (full path)\n: ")
while True:
	try:
		thefile = open(filename, 'rw+')
		break
	except:
		filename = raw_input("Please provide a valid file name (full path)\n: ")

copyordel = raw_input("Type 'c' to conserve the old file and copy, or 'ow' to overwrite\n: ")
while copyordel != 'c' and copyordel != 'ow':
	copyordel = raw_input("Type 'c' to conserve the old file and copy, or 'ow' to overwrite\n: ")

x = thefile.read()
thefile.close()
y = x.split("\n")

#map(lambda x: x*2 + 10, l)
parsed = map(lambda s: s.strip(), y)
stringparsed = "\n".join(parsed)
print stringparsed
if copyordel == 'c':
	newfilename = raw_input("Name the new file:\n ")
	newfile = open(newfilename, 'w')
	newfile.write(stringparsed)
	newfile.close()
elif copyordel == 'ow':
	thefile = open(filename, 'w')
	thefile.write(stringparsed)
	thefile.close()







