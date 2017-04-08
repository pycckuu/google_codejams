# from __future__ import print_function
import fileinput


with open('A-large-practice.in', 'r') as f:
    lines = f.read().splitlines()
c = []
i = []
p = []

# i = 0
n = int(lines[0])


def find_indeces(credit, n_items, prices):
    for l, k in enumerate(prices):
        for q, w in enumerate(prices):
            if k + w == credit and l != q:
                return l + 1, q + 1

for j in xrange(0, n):
    c.append(int(lines[1 + 3 * j]))
    i.append(int(lines[2 + 3 * j]))
    p.append([int(x) for x in lines[3 + 3 * j].split()])

f1=open('output', 'w+')

for j in xrange(0, n):
    i1,i2 = find_indeces(c[j], i[j], p[j])
    f1.write("Case #%i: %i %i\n" % (j + 1, i1, i2))
