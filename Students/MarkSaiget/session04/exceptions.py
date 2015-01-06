#! /user/bin/env python
"""Complete Exceptions section of Session 04 hw."""

"""
The raw_input() function can generate two exceptions: EOFError or
KeyboardInterrupt on end-of-file(EOF) or canceled input.
Create a wrapper function, perhaps safe_input() that returns None
rather than raising these exceptions,
when the user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for
End Of File.
"""


def safe_input(string):
    try:
        output = raw_input(string)
    except (EOFError, KeyboardInterrupt) as the_error:
        print the_error
        output = None
    return output

if __name__ == '__main__':
    print safe_input("Input text-->")
