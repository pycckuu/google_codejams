from __future__ import division
import fileinput
import re
import math

with open('D-large.in', 'r') as f:
    lines = f.read().splitlines()

f1 = open('output_t', 'w+')

n = int(lines[0])

def test(k, c, s):
    tiles = []
    if k == 1:
        tiles.append(1)
    if k == 2 and c == 1:
        tiles.append(1)
        tiles.append(2)
    if k == 2 and c > k:
        tiles.append(2)
    if k > 2:
        for i in xrange(0, c):
            tiles.append(c + (k ** (c - 1) + 1) * i)
    # print '\ndebug:',s, len(tiles)
    if k==2 and c==2 and s ==1:
        return "IMPOSSIBLE"
    if (s < math.ceil(k/c) ):
        return "IMPOSSIBLE"
    return " ".join([str(i) for i in tiles])


def line(line):
    k, c, s = line.split()
    k, c, s = int(k), int(c), int(s)
    return k, c, s


def test_all_examples():
    for i in xrange(0, n):
        k, c, s = line(lines[i+1])
        print "Case #%i:" % (i+1,), test(k, c, s)
        f1.write("Case #%i: " % (i+1,))
        f1.write(test(k, c, s)+'\n')

test_all_examples()
