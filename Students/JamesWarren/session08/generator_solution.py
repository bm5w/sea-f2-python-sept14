#!/usr/bin/env python

def intsum():
    i = 0
    n = 1
    while True:
        yield i
        i += n
        n += 1

def intsum2():
    i = 0
    n = 1
    while True:
        yield i
        i += n
        n += 1

def doubler():
    i = 1
    while True:
        yield i
        i = i*2

def fib():
    i = 1
    i1 = 1
    i2 = 2
    while True:
        yield i
        i = i1
        i1 = i2
        i2 = i + i1

def prime():
    i = 2
    while True:
        for n in range(2, i):
            if i % n == 0:
                i += 1
                break
        else:
            yield i
            i += 1
