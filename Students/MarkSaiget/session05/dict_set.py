"""dict and set comprehensions HW, session 05"""

food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

# 1. Print the dict by passing it to a string format method, so that you get
# something like:"Chris is from Seattle, and he likes chocolate cake,
# mango fruit, greek salad, and lasagna pasta"
print "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} \
salad, and {pasta} pasta".format(**food_prefs)

# 2. Using a list comprehension, build a dictionary of numbers from zero to
# fifteen and the hexadecimal equivalent (string is fine).
hexa = ["{:X}".format(num) for num in range(16)]
numbers = range(16)
dict = {}
for key, value in zip(numbers, hexa):
    dict[key] = value
print dict
# Do the previous entirely with a dict comprehension - should be a one-liner
print {num: "{:X}".format(num) for num in range(16)}

# 4. Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of 'a's in each value. You can do this either by editing
# the dict in place, or making a new one. If you edit in place, make a copy
# first!
# copy dict
copy = food_prefs.copy()
food_prefs = {key: val.count('a') for key, val in food_prefs.iteritems()}
print food_prefs

# 5. Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible 2, 3 and 4.
# A) Do this with one set comprehension for each set.
s2 = {x for x in range(21) if x % 2 == 0}
s3 = {x for x in range(21) if x % 3 == 0}
s4 = {x for x in range(21) if x % 4 == 0}
print s2, s3, s4
# B) What if you had a lot more than 3? - Don't Repeat Yourself (DRY)
# a) create a sequence that holds all three sets
s2, s3, s4 = sets = (set(), set(), set())
print sets
# b) loop through that sequence to build the sets up - so no repeated code.
for div, set in zip(range(2,6), sets):
    {set.add(x) for x in range(21) if x % div == 0}
# C)Extra credit: do it all as a one-liner by nesting a set comprehension
# inside a list comprehension. (OK, that may be getting carried away!)
s2, s3, s4 = [{x for x in range(21) if x % div == 0} for div in range(2, 5)]
