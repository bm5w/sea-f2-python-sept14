"""solution for session 04, warmup 2"""


inputted = (2, 123.4567, 10000)
print "\"file_{one}:{two}, {three}\"".\
    format(one='%.3d' % inputted[0], two='%.2f' % inputted[1], three='%.0E' % inputted[2])
