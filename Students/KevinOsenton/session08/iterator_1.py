#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


#if __name__ == "__main__":
#
#    print "first version"
#    for i in IterateMe_1():
#        print i

class IterateMe_2(object):
    def __init__(self, start, stop, step=1):
        self.start = start - step
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration

if __name__ == "__main__":
    it = IterateMe_2(2,20,2)
    
    for i in it:
        if i>10: break
        print i

    for i in it:
        print i 