def gen_fib(stop = 10):

	current = 0
	yield current
	next = 1

	yield next
	num = 0

	while num < stop:
		add = current + next
		yield add

		current = next
		next = add
		num += 1

def gen_doubler(start = 1, stop = 10):

	current = 0
	yield start

	while current < stop:
		start *= 2
		yield start
		current += 1

def gen_prime(stop = 10):
	start = 2
	yield start
	current = 0

	while current < stop:
		start += 1
		x = xrange(2,start)
		flag = True

		for i in x:
			if start % i == 0:
				flag = False
				break
		if flag == True:
			yield start
			current += 1

def gen_sum(stop = 10):
	sum = 0
	for i in xrange(stop):
		sum += i
		yield sum
	

















