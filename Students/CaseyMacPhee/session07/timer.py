
import timeit
class Timer(object):

	def __init__(self, handle_error):
		self.handle_error = handle_error
		self.start = timeit.timeit()
	def __enter__(self):
		return self
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.end = timeit.timeit()
		print self.start - self.end
		return self.handle_error

