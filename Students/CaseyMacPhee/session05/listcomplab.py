

def count_evens(nums):
    return len([i for i in nums if i % 2 == 0])
y = count_evens([2,3,4])
print y

food_prefs = {u"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

printstring = "{name} is from {city}, and he likes {cake},\
 {fruit} fruit, {salad} salad, and {pasta} pasta."

s = printstring.format(**food_prefs)
print s


x = range(16)

new_list = [hex(i) for i in x]

z = {i:j for i, j in zip(x, new_list)}
print z


y = {i: hex(i) for i in x}
print y

new_food_prefs = {}

for i in food_prefs:
	astr = 0
	val = food_prefs.get(i)
	for x in val:
		if x == 'a' or x == 'A':
			astr += 1
	new_food_prefs[i] = astr

s2 = {x for x in range(21) if x%2 == 0}
s3 = {x for x in range(21) if x%3 == 0}
s4 = {x for x in range(21) if x%4 == 0}

setbin = [{x for x in range(21) if x % i == 0} for i in range(2,5)]

def mkfunlist(n):
	funlist = []
	for i in range(n+1):
		funlist.append(lambda x, e = i: x + e)
	return funlist

