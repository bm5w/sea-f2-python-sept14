def pwrapper (string):
    def wrapper(*args, **kwargs):
        wrapped = '<p> ' + string(*args, **kwargs) + ' </p>'
        return wrapped
    return wrapper

@pwrapper
def return_a_string(string):
    return string

if __name__ == '__main__':
    print return_a_string("this is a string")