#! /usr/bin/env python
"""session 05 hw, lambda and keywork argument magic"""
"""
Write a function that returns a list of n functions, such that each one,
when called, will return the input value, incremented by an increasing number.
Use a for loop, lambda, and a keyword argument
"""


def lambda_key(n):
    out = []
    for x in range(n):
        out.append(lambda y, i=x: y+i)
    return out


# with list comprehension
def lambda_key_comp(n):
    return [lambda y, i=x: y+i for x in range(n)]


if __name__ == '__main__':
    list = lambda_key_comp(4)
    print list[0](2)
    print list[1](2)

