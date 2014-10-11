import time

class Timer(object):
    def __init__(self):
        self.handle_error = None

    def __enter__(self):
        self.start = time.time()
        return self.start

    def __exit__(self, e_type, e_val, e_traceback):
        self.end = time.time() - self.start
        print "this code took %.6f seconds" % self.end


if __name__ == '__main__':
    with Timer() as t:
        for i in range(200000):
            i = i ** 20