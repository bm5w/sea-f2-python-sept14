#! /usr/bin/env python
import string


def rot13(text):
    """Take any amount of input text and return encrypted by ROT13."""
    alpha = string.ascii_lowercase + string.ascii_uppercase
    alphaL = string.ascii_lowercase
    alphaU = string.ascii_uppercase
    alpha13 = alphaL[13:]+alphaL[:13]+alphaU[13:]+alphaU[:13]
    table = string.maketrans(alpha, alpha13)
    return text.translate(table)

if __name__ == '__main__':
        """Test rot13 function and helper functions work properly."""
        test = "The ROT13 encryption scheme is a simple substitution cyper.!?"
        print test
        print rot13(test)
