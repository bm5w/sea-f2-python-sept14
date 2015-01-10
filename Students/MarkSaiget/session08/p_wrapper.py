#! /usr/bin/env python
"""p_wrapper decorator, session 8 hw
Write a simple decorator you can apply to a function that returns a string.
Decorating such a function should result in the original output,
wrapped by an HTML 'p' tag:

In [4]: @p_wrapper
   ...: def return_a_string(string):
   ...:     return string
   ...:

In [5]: return_a_string("this is a string")
Out[5]: '<p> this is a string </p>'
Note that this is a very simple version of the very useful decorators
provided by Web Frameworks.
"""
def p_wrapper(func):
    def wrapped(*args, **kwargs):
        return '<p> {string} </p>'.format(string=func(*args, **kwargs))
    return wrapped


@p_wrapper
def return_a_string(string):
    return string

if __name__ == '__main__':

    print return_a_string(raw_input("input text to be wrapped:"))