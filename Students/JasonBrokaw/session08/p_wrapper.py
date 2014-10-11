from __future__ import unicode_literals


def p_wrapper(func):
    def wrapped(*args, **kwargs):
        result = "<p>" + func(*args, **kwargs) + "</p>"
        return result
    return wrapped


@p_wrapper
def simplestring():
    return "I am but a simple string"


def simplerstring():
    """unwrapped, for comparison"""
    return "I am but a simpler string"


if __name__ == '__main__':
    print simplestring()
    print simplerstring()
