#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_2(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, *args):
        if not args:
            self.interval = 1
            self.current = -1
            self.stop = 5
        elif len(args) == 1:
            self.stop = args[0]
            self.interval = 1
            self.current = -1
        elif len(args) == 2:
            self.stop = args[1]
            self.interval = 1
            self.current = args[0] - 1
        elif len(args) == 3:
            self.stop = args[1]
            self.interval = args[2]
            self.current = args[0] - self.interval

    def __iter__(self):
        return self

    def next(self):
        self.current += self.interval
        if (self.stop - self.current) * self.interval > 0:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print "updated version, should print 2, 4, ... 18"
    for i in IterateMe_2(2, 20, 2):
        print i

    print "Testing break, these two numbers should be the same (12)"
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
    print i

    it = xrange(2, 20, 2)
    for i in it:
        if i > 10:  break
    print i



