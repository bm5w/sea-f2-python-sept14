import math

def sum_int(n):
    num = 1
    while num <= n:
        yield sum(range(num))
        num += 1

def doubler(n):
    num = 1
    while num <= n:
        yield num
        num *= 2

def fib(n):
    seq_len = 0
    prev = 0
    curr = 1

    while seq_len < n:
        yield curr
        curr += prev
        prev = curr
        seq_len += 1

def prime():
    primes = [2]
    num = 3
    while True:
        for prime in primes:
            if num % prime == 0 or num % prime == 2:
                break
            if num % prime not in primes:
                yield num
                primes.append(num)
        num += 2







