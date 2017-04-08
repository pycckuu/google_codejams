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


def reverse_number(n):
    return int((str(n))[::-1])


def count(start):
    n = 0
    while start > 0:
        m = {}
        # print "n:", n, "; start:",start
        if start == 1:
            return n + 1
        if start < 20:
            return n + start
        m[10] = start - 10
        for i in xrange(1, 11):
            if (start - i) % 10 != 0 and (start - i) > 0:
                m[i] = reverse_number(start - i)
        # print m
        k = min(m, key=m.get)
        if start - 10 < m[k]:
            n += 10
            start = start - 10
        else:
            n += k + 1
            start = m[k]
    return n

if __name__ == '__main__':
    lines = read_file("A-small-practice.in")
    t = int(lines[0])
    for x in xrange(1, t + 1):
        write_output(x, count(int(lines[x])))
    # print count(1101)
    # print 20%10 !=0
