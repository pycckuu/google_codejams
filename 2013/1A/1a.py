from __future__ import division
from collections import Counter
import itertools
import math


def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return lines


def advanced_read_file(file_name):
    lines = read_file(file_name)
    n = int(lines[0])
    size = []
    examples = []
    lines = lines[1:]
    for i in xrange(n):
        N = int(lines[0])
        lines = lines[1:]
        size.append(N)
        examples.append(lines[:2 * N - 1])
        lines = lines[2 * N - 1:]
    return size, examples


def write_output(n_case, res):
    print("Case #%d: %s" % (n_case, res))


def one_ring(r):
    # pi*((r+2)^2 - r^2)/2pi = 1+2r
    return 2 + 2 * r


def how_many_rings(r_start, t):
    r_start, t = int(r_start), int(t)
    sum = 0
    i = 0
    while sum <= t:
        sum += one_ring(r_start)
        r_start += 2
        i += 1
    return i - 1


def arifmetic_sum_full_ring(t):
    # n/2(2*a+(n-1)*d) = sum of arithmetic progression
    n = 1 / 2 * (-1 + math.sqrt(1 + 4 * t))
    return n


def innner_circle(r_start):
    # n = 1 / 2 * (-1 + math.sqrt(1 + 4 * t))
    s = r_start / 2 * (2 * 0 + (r_start - 1) * 2) / 2
    return s


def how_many_rings_advanced_version(r, t):
    return 1 / 2 * (-1 + math.sqrt(1 + 4 * (t + innner_circle(r))))


# def multiple_output(n, fun):
#     for i in xrange(n):
#         write_output(i + 1, fun(lines[i + 1]))

if __name__ == '__main__':
    lines = read_file("example.in")
    r, t = lines[4].split()
    print int(how_many_rings(int(r), int(t)))
    # print innner_circle(4)
