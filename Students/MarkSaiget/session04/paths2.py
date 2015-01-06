#! /usr/bin/env python
"""
a program which copies a file from a source, to a destination
(without using shutil, or the OS copy command)
"""
import io


def copyFile(source, dest):
    src = io.open(source, 'rb')
    outfile = io.open(dest+source, 'wb')
    outfile.write(src.read())
    src.close()
    outfile.close()

if __name__ == '__main__':
    source = \
        u'sherlock.txt'
    destination = \
        u'/home/mark/f2_wd/sea-f2-python-sept14/Students/MarkSaiget/session04/test/'
    copyFile(source, destination)
