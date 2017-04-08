from __future__ import division
import fileinput
import re

with open('workfile.in', 'r') as f:
    lines = f.read().splitlines()

f1 = open('output_t', 'w+')

n = int(lines[0])


lenght_of_number = int(lines[1].split()[0])
uniqueness = int(lines[1].split()[1])

string = lenght_of_number * '0'
list_string = list(string)
list_string[0] = '1'
list_string[-1] = '1'
init_string = "".join(list_string)


def find_devisor_in_base(n):
    if n < 2 or n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return f
        if n % (f + 2) == 0:
            return f + 2
        f += 6
    return False


def check_deviders(string):
    deviders = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False}
    for base in xrange(2, 11):
        number_in_base = int(string, base)
        deviders[base] = find_devisor_in_base(number_in_base)
    if any(v is False for v in deviders.itervalues()):
        return -1
    else:
        return deviders


def iterate_string(init_string, uniqueness):
    strings = []
    i = 0
    for number in xrange(int(init_string, 2), 2**len(init_string), 2):
        deviders = check_deviders(str_base_2(number))
        if deviders != -1:
            strings.append([str_base_2(number), deviders])
            i += 1
            if i >= uniqueness:
                return strings


def str_base_2(number):
    length = len(str(number))
    strFormat = "{0:0%db}" % length
    res = strFormat.format(number)
    return res


result = iterate_string(init_string, uniqueness)

for j in xrange(1, n + 1):
    print "Case #%i:" % (j,)
    for i in result:
        print i[0] + " " + " ".join([str(i) for i in i[1].values()])


# print lenght_of_number, uniqueness, string


# for j in xrange(1, n + 1):
# print lines[j].count('-')
#     p = re.compile('[-]+')
#     counter =  2*len(p.findall(lines[j]))
#     if lines[j][0] == '-': counter-=1
# f1.write("Case #%i: %s\n" % (j, counter))
# print ("Case #%i: %s" % (j, counter))
