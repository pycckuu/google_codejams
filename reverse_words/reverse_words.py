# from __future__ import print_function
import fileinput


with open('B-large-practice.in', 'r') as f:
    lines = f.read().splitlines()

n = int(lines[0])

f1=open('output', 'w+')

for j in xrange(1, n+1):
    f1.write("Case #%i: %s\n" % (j, " ".join([x for x in reversed(lines[j].split())])))