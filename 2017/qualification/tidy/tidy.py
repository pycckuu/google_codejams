import sys

sys.setrecursionlimit(150000000)


def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return lines


def find_tidy_number(s):
    rev_s = s[::-1]
    for i in range(len(s) - 1):
        if rev_s[i] >= rev_s[i + 1]:
            next
        else:
            if int(s) > 0:
                find_tidy_number(str(int(s) - 1))
            else:
                "IMPOSSIBLE"
    return(s)


def find_tidy_number_no_rec(s):
    while int(s) > 0:
        if len(s) == 1:
            return s
        rev_s = s[::-1]
        for i in range(len(s) - 1):
            if rev_s[i] >= rev_s[i + 1]:
                if i == len(s) - 2:
                    return s
            else:
                break
        n = int(s)
        n -= 1
        s = str(n)


def big_find_tidy_number(s):
    if len(s) == 1:
        return int(s)
    i = 0
    while i < (len(s)):
        if s[i] <= s[i + 1]:
            i += 1
            if i == len(s) - 1:
                return int(s)
        else:
            s = s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i - 1)
            i = 0
    return int(s)

if __name__ == '__main__':
    lines = read_file("B-large.in")
    for n in range(0, int(lines[0])):
        string = lines[n + 1]
        print("Case #%d: %s" % (n + 1, big_find_tidy_number(string)))
