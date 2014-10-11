#!/usr/bin/env python

def p_wrapper(func):
    def wrapper(text):
        return "<p>%s</p>" % text
    return wrapper

@p_wrapper
def return_a_string(text):
    return text

print return_a_string("This is a wrapper test.")