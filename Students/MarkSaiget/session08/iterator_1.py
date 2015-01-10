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


class IterateMe_2(IterateMe_1):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, start, stop, step=1):
        super(IterateMe_2, self).__init__(stop)
        self.start = start-step
        self.current = start-step
        self.step = step
    def __iter__(self):
        self.current = self.start
        return self
    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == "__main__":


    a = IterateMe_2(2, 20, 2)
    b = xrange(2, 20, 2)
    for x, y in zip(a, b):
        if y > 10: break
        print x, y
    for x, y in zip(a, b):
        print x, y
