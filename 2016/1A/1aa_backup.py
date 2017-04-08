from collections import defaultdict


def DFS(G, v, seen=None, path=None):
    if seen is None:
        seen = []
    if path is None:
        path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen, t_path))
    return paths


def longest_path(edges):
    G = defaultdict(list)
    for (s, t) in edges:
        G[s].append(t)
        G[t].append(s)

    all_paths = {}
    for i in xrange(0, len(edges)):
        all_paths[i] = DFS(G, str(i+1))
        # print DFS(G, str(i+1))
    print all_paths
    max_path = 0
    
    for k,v in all_paths.iteritems():
        temp = len(max(v, key=lambda l: len(l)))
        if temp > max_path:
            max_path = temp
    return max_path
    # print("All Paths:")
    # print(all_paths)
    # print("Longest Path:")
    # print(max_path)
    # print("Longest Path Length:")
    # print all_paths


# edges = [['1', '3'], ['2', '3'], ['3', '4'], ['4', '3']]

# print longest_path(edges)


file_name = "example.in"
with open(file_name, 'r') as f:
    lines = f.read().splitlines()

n = int(lines[0])
# for i in xrange(0, n):
i = 1
line_1 = lines[1 + i*2]
line_2 = lines[2 + i*2 ]
e = line_2.split()
edges = []
for j in xrange(0, len(e)):
    edges.append([str(j+1),str(e[j])])

print edges
# print longest_path(edges)
print("Case #%d: %s" % (i + 1, longest_path(edges)))

#     line_3 = lines[3 + i * 3]
    # print("Case #%d: %s" % (i + 1, test_example(line_1, line_2, line_3)))