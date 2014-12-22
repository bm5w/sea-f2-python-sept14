def ack(m, n):
    """Perform Ackermann function, where function is not defined for input values less than 0."""
    #Check inputs are greater than zero.
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))
print ack(1, 4)