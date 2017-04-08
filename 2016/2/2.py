from __future__ import division
from collections import Counter
import itertools


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
        examples.append(lines[:2*N-1])
        lines = lines[2*N-1:]
    return size, examples

def write_output(n_case, res):
    print("Case #%d: %s" % (n_case, res))


def multiple_output(n, fun):
    for i in xrange(n):
        write_output(i + 1, fun(lines[i + 1]))


if __name__ == '__main__':
    size, examples = advanced_read_file("B-large-practice.in")

    final_res = []
    for i in xrange(len(size)):
        N = size[i]
        lists = [l.split() for l in examples[i]]

    # lists = []
    # for j in xrange(1, 2 * N):
    #     lists.append([int(ch) for ch in lines[j + 1].split()])
        flat_lists = list(itertools.chain(*lists))
        unique = set(flat_lists)
        res = []
        for e in unique:
            if not flat_lists.count(e) % 2 == 0:
                res.append(int(e))
        res.sort()
        final_res.append(res)
        write_output(i+1, " ".join(str(x) for x in res))
