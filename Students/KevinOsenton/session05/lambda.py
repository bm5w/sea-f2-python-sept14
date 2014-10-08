def function_builder(n):
    new_list = [lambda x, y=k: x + y for k in range(n)]
    return new_list

the_list = function_builder(4)
print the_list[0](2)
print the_list[1](2)
for f in the_list:
    print f(5)
