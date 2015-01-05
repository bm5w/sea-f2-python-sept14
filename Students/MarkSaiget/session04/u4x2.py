"""solution for session 04, warmup 2"""


from decimal import Decimal

inputted = (2, 123.4567, 10000)
three = '%.0E' % Decimal(inputted[2])
print "\"file_00{one}:{two}, {three}\"".\
    format(one=inputted[0], two=round(inputted[1], 2), three=three)
