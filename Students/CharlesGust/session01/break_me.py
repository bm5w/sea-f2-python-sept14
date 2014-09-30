import math

def raiseNameError():
    return aNameThatCannotBeFound


def raiseTypeError():
    return -"NotANumber"


def raiseSyntaxError():
    """returnn 0"""


def raiseAttributeError():
    return math.truncate(1.0)

raiseNameError()
raiseTypeError()
"""raiseSyntaxError()"""
raiseAttributeError()
