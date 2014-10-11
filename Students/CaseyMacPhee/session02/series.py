def fibonacci(n):
	"""Returns the number at the n'th place in the fibonacci sequence"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
	"""Returns the number at the n'th place in the lucas sequence"""
	if n == 0:
		return 0
	elif n == 1:
		return 2
	elif n == 2:
		return 1
	else:
		return lucas(n-1) + lucas(n-2)



def sum_series(n, first=0, second=1):
	"""Returns the number at the n'th place in the given sequence.
	If no second, and third arguments are given, the function will default 
	to the fibonacci function"""

	if n == 0:
		return first
	elif n == first:
		return first
	elif n == second:
		return second
	else: 
		return sum_series(n-1, first, second) + sum_series(n-2, first, second)




	
