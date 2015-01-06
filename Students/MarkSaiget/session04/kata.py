"""
Implement trigram algorithm that generates a couple hundred words of text
using  sherlock holmes (sherlock.txt) as input.
"""


import io

# Read in sherlock.txt
header_size = 1193
f = io.open('sherlock.txt', encoding='utf-8')
# remove header
header = f.read(header_size)
sherlock = f.read()
f.close
text = sherlock[:1000].strip()
text = text.replace('\n', ' ')          # remove \n values


# Generate dictionary
start = 0
firstSpace = text.index(u' ')
keepGoing = True
dict = {}
while keepGoing:
    secondSpace = text.find(u' ', firstSpace+1)
    thirdSpace = text.find(u' ', secondSpace+1)
    dict[text[start:secondSpace].strip()] = \
        text[secondSpace+1:thirdSpace].strip()
    if text.find(u' ', thirdSpace) == -1:  # if no more spaces left, stop loop
        keepGoing = False
    start = firstSpace
    firstSpace = secondSpace
print text
print dict
