import numpy

def fast_power(a,n):
    """
    This function assumes that n >= 0
    """
    result = 1
    value = a
    power = n
    while power > 0:
        if power % 2 == 1:
            result = result * value
        value = value * value
        power = power//2
    return result

def nump_p(x,a):
    numpy.power(x,a)

print(nump_p( (3+5**0.5), 100000 ))
