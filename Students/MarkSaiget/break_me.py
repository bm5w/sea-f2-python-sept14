# Functions to create each of the exceptions below
# Homework Session 1, Task 4

def name_error():
    test
#name_error()

def type_error():
    x= 'test'
    y = x%2
# type_error()

# def syntax_error():
#     test ='test'
#     prin test
#syntax_error()

# attribute error.  can be trying to modifiy read-only attribute
# or  referencing an attribute that doesn't exist
def attribute_error():
    pass
test =attribute_error()
test.attribute