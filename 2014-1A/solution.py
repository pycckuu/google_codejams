import itertools

import numpy as np


def read_init_and_form_matrices(line_2, line_3):
    ishod = np.array([[int(ch) for ch in v]for v in line_2.split()])
    req = np.array([[int(ch) for ch in v] for v in line_3.split()])
    return ishod, req


def modify_rows(ishod, req, N, L):
    counter = 0
    list_of_column_equal_0_and_1 = []
    for i in xrange(0, L):
        if sum(req[:, i]) == sum(ishod[:, i]):
            pass
        elif sum(req[:, i]) == N - sum(ishod[:, i]):
            counter += 1
            ishod[:, i] = np.logical_not(ishod[:, i])
        elif sum(req[:, i]) == N - sum(ishod[:, i]) and sum(req[:, i]) == sum(ishod[:, i]):
            list_of_column_equal_0_and_1.append(i)
        else:
            return ishod, counter, list_of_column_equal_0_and_1, False
    return ishod, counter, list_of_column_equal_0_and_1, True


def second_test(modified_ishod, req, N):
    test = 0
    for i in xrange(0, N):
        for j in range(0, N):
            if all(modified_ishod[i,:] == req[j,:]):
                test += 1
                break

    if test == N:
        return True
    else:
        return False


def rotation_of_equal_sized_columns(i, r, c, l):
    for i in xrange(2, len(l)):
        for a in itertools.combinations(l, i):
            temp_ishod = np.array(i, copy=True)
            for column in a:
                temp_ishod[:, column] = np.logical_not(temp_ishod[:, column])
            if second_test(temp_ishod, r):
                c = c + len(a)
                return c, True
    return c, False


def test_example(line_1, line_2, line_3):
    N, L = map(int, line_1.split())
    ishod, req = read_init_and_form_matrices(line_2, line_3)
    req, c, l, p = modify_rows(ishod, req, N, L)
    if not p:
        return "NOT POSSIBLE"
    if second_test(ishod, req, N):
        return c
    c, p = rotation_of_equal_sized_columns(ishod, req, c, l)
    if p:
        return c
    else:
        return "NOT POSSIBLE"


def run():
    file_name = "in.txt"
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    n = int(lines[0])
    for i in xrange(0, n):
        line_1 = lines[1 + i * 3]
        line_2 = lines[2 + i * 3]
        line_3 = lines[3 + i * 3]
        print("Case #%d: %s" % (i + 1, test_example(line_1, line_2, line_3)))

if __name__ == '__main__':
    run()
