from __future__ import division
import sys

# file_name = sys.argv[1]

# with open(file_name, 'r') as f:
with open('B-small-practice.in', 'r') as f:
    lines = f.read().splitlines()

n = int(lines[0])


B = int(lines[1].split()[0])
N = int(lines[1].split()[1])
Mk = [int(i) for i in lines[2].split()]


def test_case(B, N, Mk, k):
    time_i = {i: 0 for i in range(1, B + 1)}
    speed_i = {i: Mk[i - 1] + 1e-6 * i for i in range(1, B + 1)}
    for j in range(0, N - 1):
        time_i[min(time_i, key=time_i.get)] = time_i[min(time_i, key=time_i.get)] + speed_i[min(time_i, key=time_i.get)]
    print  min(time_i, key=time_i.get)

for i in range(0, n):
    B = int(lines[1 + 2 * i].split()[0])
    N = int(lines[1 + 2 * i].split()[1])
    Mk = [int(i) for i in lines[2 + 2 * i].split()]
    test_case(B, N, Mk, i)


# time_i[min(time_i, key=time_i.get)] = time_i[min(time_i, key=time_i.get)]+ speed_i[min(time_i, key=time_i.get)]
# print(time_i)

# time_i[min(time_i, key=time_i.get)] = time_i[min(time_i, key=time_i.get)] +speed_i[min(time_i, key=time_i.get)]
# print(time_iv
