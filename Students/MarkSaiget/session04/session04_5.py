# Create a set with the letters in 'Python' and add 'i' to the set.
# string = "Python"
pythonSet = set(u'Python')
# for index in range(len(string)):
#     pythonSet.update([string[index]])
pythonSet.add('i')
print pythonSet

# Create a frozenset with the letters in 'marathon'
# string = "marathon"
# marathon = []
# for index in range(len(string)):
#     marathon.append(string[index])
fs = frozenset(u'marathon')
print fs

# display the union and intersection of the two sets.
print "union of two sets: ", pythonSet.union(fs)
print "intersection of two sets: ", pythonSet.intersection(fs)