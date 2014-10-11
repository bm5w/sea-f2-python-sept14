def intsum():
    i = 1
    while True:
        yield sum(range(i))
        i += 1

def intsum2():
    sum = 0
    counter = 1
    while True:
        yield sum
        sum += counter
        counter += 1

def doubler():
    value = 1
    while True:
        yield value
        value *= 2

def fib():
    previous = 0
    current = 1
    while True:
        yield current
        previous, current = current, previous + current

def prime():
    yield 2
    knownprimes = {2}
    testing = 3
    while True:
        is_prime = True
        for prime in knownprimes:
            if not testing % prime:
                is_prime = False
                break
        if is_prime:
            knownprimes.add(testing)
            yield testing
        testing += 2


                

