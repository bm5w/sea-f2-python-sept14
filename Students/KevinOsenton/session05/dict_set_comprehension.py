food_prefs = {'name': 'Chris',
              'city': 'Seattle',
              'cake': 'chocolate',
              'fruit': 'mango',
              'salad': 'greek',
              'pasta': 'lasagna'}

#1
print ("{name} is from {city}, and he likes {cake} cake, {fruit} fruit,"
        " {salad} salad, and {pasta} pasta".format(**food_prefs))

#2
hexlist = [[x,hex(x)] for x in range(16)]
print hexlist
#3
hexdict = {x: hex(x) for x in range(16)}
print hexdict

#4
num_a = {key: value.count('a') for (key, value) in food_prefs.iteritems()}
print num_a

#5
divisible = 2
while divisible < 5:
    set_divisible = set(x for x in range(21) if x%divisible == 0)
    divisible += 1
    print set_divisible