#!/usr/bin/env python
import sys
import io
import string
#I kind of went crazy with the naming scheme...
message = """ This program strips off all that annoying whitespace. If you want to write a new file, plug that new file name in, otherwise I will just take all the whitespace out of the original file."""
file_coming_in = "session05/white_space.txt"
file_goin_out = "session05/new_white_spcae.txt"

def trash_the_whitespaces(file_coming_in, file_goin_out):
    #In this one, I'm using a map funtion
    file_in = io.open(file_coming_in).readlines()
    file_out = map(string.strip, file_in)
    file_is_out = io.open(file_goin_out, 'w')
    for line in file_out:
        file_is_out.write(line+"\n")


def trashing_with_a_list_comp(file_coming_in, file_goin_out):
    #I'm using a list comprehesion for this one
     file_in = io.open(file_coming_in).readlines()
     file_out = [line.strip()+"\n" for line in file_in]
     io.open(file_goin_out, 'w').writelines(file_out)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print message
        sys.exit(1)
    else:
        file_coming_in = sys.argv[1]
        try:
            file_goin_out = sys.argv[2]
        except IndexError:
            file_goin_out = file_coming_in
    trash_the_whitespaces(file_coming_in,file_goin_out)
    trashing_with_a_list_comp(file_coming_in, file_goin_out)