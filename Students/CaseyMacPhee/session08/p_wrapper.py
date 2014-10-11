def p_wrapper(a_function):
	def innerp(a_function):
		str = "<p>"
		str2 = "</p>"
		return str + a_function + str2
	return innerp