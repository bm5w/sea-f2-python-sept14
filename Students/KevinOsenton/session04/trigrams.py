#!/usr/bin/env python

import urllib, string, random

text_file = urllib.urlopen(raw_input("Copy and paste txt url: "))

#How would you dry this out?
read_text = text_file.read()
read_text = read_text.replace(".", "")
read_text = read_text.replace(",", "")
read_text = read_text.replace("--", " ")
read_text = read_text.replace("'", "")
read_text = read_text.replace("(", "")
read_text = read_text.replace(")", "")
read_text = read_text.lower()

word_split = read_text.split()

trigrams = {}

for i in range(len(word_split)-2):
    word_pair = tuple(word_split[i:i+2])
    trigrams.setdefault(word_pair, []).append(word_split[i+2])

#10 sentences with 10 pairs of values
dictList = []
for key, value in trigrams.iteritems():
    dictList.append(key)

sent_list = []
for i in range(10):
    temp = []
    for j in range(10):
        spot = random.randint(0,100)
        temp.append(" ".join(dictList[spot]))
    sent_list.append(" ".join(temp))

for i in sent_list:
    print i





 
