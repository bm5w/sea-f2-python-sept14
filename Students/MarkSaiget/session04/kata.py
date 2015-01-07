#! /usr/bin/env python
"""
Implement trigram algorithm that generates a couple hundred words of text
using  sherlock holmes (sherlock.txt) as input.
"""


import io
import random

# Read in sherlock.txt
header_size = 1193
f = io.open('sherlock.txt', encoding='utf-8')
# remove header
header = f.read(header_size)
sherlock = f.read()
f.close
text = sherlock.strip()
text = text.replace('\n', ' ')          # remove \n values

# Generate dictionary
start = 0
firstSpace = text.index(u' ')
keepGoing = True
dict = {}
while keepGoing:
    secondSpace = text.find(u' ', firstSpace+1)
    thirdSpace = text.find(u' ', secondSpace+1)
    key = text[start:secondSpace].strip()
    value = text[secondSpace+1:thirdSpace].strip()
    # # check if key exists already
    # if key in dict:
    #     dict[key].append(value)
    # else:
    #     dict[key] = [value]
    dict.setdefault(key, []).append(value)
    if text.find(u' ', thirdSpace) == -1:  # if no more spaces left, stop loop
        keepGoing = False
    start = firstSpace
    firstSpace = secondSpace

# Generate output
output = ['Sherlock', 'Holmes']
random.shuffle(dict['Sherlock Holmes'])
output.append(dict['Sherlock Holmes'].pop())
untilPeriod = True
while untilPeriod:
    lookup = u" ".join(output[len(output)-2:])
    if lookup in dict:
        random.shuffle(dict[lookup])        # shuffle values to get random
        output.append(dict[lookup].pop())
    else:
        output.append(output.pop().strip() + ('.'))
        untilPeriod = False

print u" ".join(output)
