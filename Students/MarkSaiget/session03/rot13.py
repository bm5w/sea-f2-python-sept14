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
    test = "The ROT13 encryption scheme is a simple substitution cyper.?1!"
    test_output = "Gur EBG13 rapelcgvba fpurzr vf n fvzcyr fhofgvghgvba plcre.?1!"
    assert rot13(test) == test_output
    test2 = "Rot13 or Rot-13 (short for rotate 13) is a simple letter substitution encryption scheme. It works by replacing the current english letters in a message with those that are 13 positions ahead in the alphabet. For example, the letter a is replaced by n, b by o, c by p, etc. Numbers and punctuation are not encoded."
    test2_output = "Ebg13 be Ebg-13 (fubeg sbe ebgngr 13) vf n fvzcyr yrggre fhofgvghgvba rapelcgvba fpurzr. Vg jbexf ol ercynpvat gur pheerag ratyvfu yrggref va n zrffntr jvgu gubfr gung ner 13 cbfvgvbaf nurnq va gur nycunorg. Sbe rknzcyr, gur yrggre n vf ercynprq ol a, o ol b, p ol c, rgp. Ahzoref naq chapghngvba ner abg rapbqrq."
    assert rot13(test2) == test2_output
    print u"All tests pass."
