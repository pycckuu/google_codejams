from __future__ import division
from collections import Counter
import itertools
import math


def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return lines



if __name__ == '__main__':

    a = '?2?'
    b = '??3'
    x,y = a, b
    # list = []
    x = x.replace('?', "0")
    y = y.replace('?', "0")
    if int(x)>int(y):
        a = a.replace('?', "0")
        b = b.replace('?', "9")
    else:
        b = b.replace('?', "0")
        a = a.replace('?', "9")

    print a,b
    # for i in xrange(len(a)):
    #     if (b[i]!='?') and (a[i]!='?'):
    #         print a[i], b[i]
    #         list.append([i,a[i]>b[i]])
    #     if a[i]=='?' and b[i]!='?':
    #         a[i] = b[i]
    #     if b[i]=='?' and a[i]!='?':
    #         b[i] = a[i]
    #     if (b[i]=='?') and (a[i]=='?'):
    #         x[i], y[i]= "0","0"



    # a = "".join(a)
    # b = "".join(b)



    # # if not list:
    #     # a = a.replace('?', "0")
    #     # b = b.replace('?', "0")
    # # else:

    # print "".join(a), "".join(b)

    # lines = read_file("B1.in")
    # for n in xrange(0, int(lines[0])):
    # # n = 98
    #     string = lines[n + 1]
    #     print("Case #%d: %s" % (n + 1, find_numbers(string)))

