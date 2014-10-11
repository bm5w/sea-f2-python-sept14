#!/usr/bin/env python

from __future__ import unicode_literals
import time, sys, io

class Timer(object):
    def __init__(self, outfile=sys.stdout):
        self.handle_error = False
        self.outfile = outfile
    def __enter__(self):
        self.starttime = time.time()
        return self.starttime
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.starttime
        self.outfile.write('this code took %.6f seconds' % self.elapsed)
        return self.handle_error

if __name__ == '__main__':
    with Timer() as t:
        for i in range(200000):
            i = i ** 20

    with Timer(io.open("timelog.txt", 'w')) as t:
        for i in range(300000):
            i = i ** 20
