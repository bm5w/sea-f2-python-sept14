# Create a dictionary containing "name", "city", and "cake" for "Chris" from
# "Seattle" who likes "Chocolate".
dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
# Display the dictionary.
print dict
dict.pop('cake')            # Delete the entry for "cake".
# Display the dictionary.
print dict
# Add an entry for "fruit" with "Mango" and display the dictionary.
dict['fruit'] = 'Mango'
print dict.keys()                    # Display the dictionary keys.
print dict.values()                 # Display the dictionary values.
# Display whether or not "cake" is a key in the dictionary (i.e. False) (now).
print 'cake' in dict
# Display whether or not "Mango" is a value in the dictionary.
bool = False
for value in dict.itervalues():
    if value == 'Mango':
        bool = True
print bool

# or
print 'Mango' in d.values()
