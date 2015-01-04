msg = []
num = 6
for item in range(1, num+1):
    msg.append(str(item))
numbers = u", ".join(msg)
print "the first {num} numbers are: {numbers}".format(num=num, numbers=numbers)
