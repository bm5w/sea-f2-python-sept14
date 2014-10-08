#series 1
description = {'name': 'Chris',
               'city': 'Seattle', 
               'cake': 'Chocolate'}
print description
del description['cake']
print description
description['fruit'] = 'Mango'
print description
if 'cake' in description:
    print 'True'
else:
    print 'False'
if 'Mango' in description.values():
    print 'True'
else:
    print 'False'

#series 2
numbers = {}
for i in range(16):
    numbers[i] = hex(i)
print numbers

#series 3
num_a = {}
for key in description:
    a_count = 0
    for char in description[key]:
        if char == 'a':
            a_count += 1
    num_a[key] = a_count
print num_a

#series 4
test_list = range(21)
s2 = set()
s3 = set()
s4 = set()
for i in test_list:
    if i%2 == 0:
        s2.add(i)
    if i%3 == 0:
        s3.add(i)
    if i%4 == 0:
        s4.add(i)
print s2
print s3
print s4
print s3.issubset(s2)
print s4.issubset(s2)

#series 5
python_set = set('python')
python_set.add('i')
marathon_set = frozenset('marathon')
print python_set.union(marathon_set)