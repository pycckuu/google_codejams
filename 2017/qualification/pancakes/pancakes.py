

def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    return lines


def tripplets(cakes, flipper):
    pattern = '0' * int(flipper)
    repl = '1' * int(flipper)
    return re.sub(pattern, repl, cakes), len(re.findall(pattern, cakes))


def rest(cakes, flipper):
    i = 0
    while i < len(cakes):
        print(cakes)
        if cakes[i] == '-' and len(cakes[i:]) >= int(flipper):
            s = ''
            for ch in cakes[i:i + int(flipper)]:
                if ch == '-':
                    s += '+'
                else:
                    s += '-'
            i = 0
            cakes = cakes[:i] + s + cakes[i + int(flipper):]
        else:
            i += 1
    print(cakes)


def prepare_data(cakes):
    new_cakes = []
    for ch in cakes:
        if ch == '-':
            new_cakes.append(0)
        else:
            new_cakes.append(1)
    return new_cakes


def produce_all_possible_variants(cakes):
    if sum(d) == len(cakes):
        return 0
    variants = [[cakes]]
    for i in cakes:
        print(i)


def flip(cakes, flipper):
    cakes = cakes.replace('-', '0')
    cakes = cakes.replace('+', '1')

    cakes, a = tripplets(cakes, flipper)
    # print(cakes)
    for i in range(len(cakes) - int(flipper)):
        s = cakes[i:i + int(flipper)]
        # print(s)
        if len(re.findall("0+", s)) > 1:
            return 'IMPOSSIBLE'
    return a + len(re.findall("0+", cakes))

if __name__ == '__main__':
    import re

    lines = read_file("A-small-attempt0.in")
    # for n in range(0, int(lines[0])):
    n = 98
    cakes, flipper = lines[n + 1].split()
    print(cakes, flipper)
    print("Case #%d: %s" % (n + 1, flip(cakes, flipper)))

    # d = prepare_data(cakes)
    # rest(cakes, flipper)
