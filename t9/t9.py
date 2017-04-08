# from __future__ import print_function
import fileinput


with open('C-large-practice.in', 'r') as f:
    lines = f.read().splitlines()

n = int(lines[0])

f1 = open('output', 'w+')


t9_dict = {"a": 2, "b": 22, "c": 222, "d": 3, "e": 33, "f": 333, "g": 4, "h": 44, "i": 444, "j": 5, "k": 55, "l": 555, "m": 6, "n": 66, "o": 666, "p": 7, "q": 77, "r": 777, "s": 7777, "t": 8, "u": 88, "v": 888, "w": 9, "x": 99, "y": 999, "z": 9999, " ": 0}


def type_string(string):
    key_list = [str(t9_dict[x]) for x in string]
    return is_pause(key_list)


def is_pause(key_list):
    new_string = key_list[0]
    for i, x in enumerate(key_list):
        if i > 0:
            if key_list[i][0] == key_list[i - 1][0]:
                new_string += " "
            new_string += x
    return new_string


for j in xrange(1, n + 1):
    # f1.write("Case #%i: %s\n" % (j, " ".join([x for x in reversed(lines[j].split())])))
    string = type_string(lines[j])
    f1.write("Case #%i: %s\n" % (j, string))
