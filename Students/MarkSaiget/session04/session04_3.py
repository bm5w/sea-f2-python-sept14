"""Using the dictionary from item 1: Make a dictionary using the same keys but
with the number of 'a's in each value."""

# dict from item 1
dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

dict2 = {}
for keys in dict.iterkeys():
    dict2[keys] = dict[keys].count("a")
print dict2

# better
for key, val in dict.items():
    dict2[key] = val.count('a')