from __future__ import division


def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return lines


def write_output(n_case, res):
    print("Case #%d: %s" % (n_case, res))


def multiple_output(n, fun):
    for i in xrange(n):
        write_output(i + 1, fun(lines[i + 1]))


def game(S):
    result = S[0]
    # for i in xrange(1, len(S)):
    #     for w in result[-2**(i - 1):]:
    #         s1, s2 = create_possible_words(w, S[i])
    #         result.append(s1)
    #         result.append(s2)
    # res = result[-2**(len(S) - 1):]
    # res.sort()
    # return res[-1]
    for i in xrange(1, len(S)):
        if S[i]<result[0]:
            result = result + S[i]
        else:
            result = S[i] + result
    return result




def create_possible_words(s, w):
    s1 = w + s
    s2 = s + w
    return s1, s2


if __name__ == '__main__':
    lines = read_file("./A-large-practice.in")
    n = int(lines[0])
    multiple_output(n, game)
