def fun_builder(n):
	the_list = []
	for f in range(n):
		the_list.append(lambda x, f=f: x+f)
	return the_list

lists = fun_builder(5)

for i in lists:
	print i(0)

#use a keyword arguement to make the_list start at 0 every time
#probably a **kwargs   self?