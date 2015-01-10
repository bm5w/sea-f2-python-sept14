#! /usr/bin/env python
"""session 08 hw, timing context manager, to learn Decorators
Create a context manager that will print to stdout the elapsed time taken to
run all the code inside the context:
    In [3]: with Timer() as t:
       ...:     for i in range(100000):
       ...:         i = i ** 20
       ...:
    this code took 0.206805 seconds

Extra Credit: allow the Timer context manager to take a file-like object as an 
argument (the default should be sys.stdout). 
The results of the timing should be printed to the file-like object.
"""
import time
import sys
import io

class Timer(object):
    def __init__(self, file=sys.stdout):
        self.out = file
        self.handle_error = True
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time()-self.start
        self.out.write(u'this code took {0:.6f} seconds\n'.format(elapsed))
        return self.handle_error

if __name__ == '__main__':
    with Timer(io.open("a.txt", 'w')) as t:
        for i in range(100000):
            i = i * 20

