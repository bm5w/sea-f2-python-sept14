# Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible 2, 3 and 4.


def makeList(denom):
    list = []
    for x in range(21):
        if x % denom == 0:
            list.append(x)
    return list

s2 = set(makeList(2))
s3 = set(makeList(3))
s4 = set(makeList(4))

# Display the sets.
print "set s2:", s2
print "set s3:", s3
print "set s4:", s4

# Display if s3 is a subset of s2 (False)
print s3.issubset(s2)
# and if s4 is a subset of s2 (True).
print s4.issubset(s2)
