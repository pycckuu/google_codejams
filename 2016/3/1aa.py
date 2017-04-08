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
            paths.append(t_path)
            paths.extend(DFS(G, t, seen, t_path))
    return paths


def longest_path(edges):
    G = defaultdict(list)
    for (s, t) in edges:
        G[s].append(t)
        # G[t].append(s)

    # print G
    all_paths = []

    for i in xrange(0, len(edges)):
        all_paths.append(DFS(G, str(i + 1)))
    # max_path = max(all_paths, key=lambda l: len(l))
    temp = 0
    # print all_paths
    for i in xrange(0, len(all_paths)):
        for path in all_paths[i]:
            # print path
            # print G[path[0]] , path[-1] , G[path[0]] , path[1] , G[path[-1]] , path[0] , G[path[-1]] , path[-2]
            if (path[0] in G[path[-1]]) or (path[-1] in G[path[0]]):
                if len(path) > temp:
                    temp = len(path)
            if (path[-2] in G[path[-1]] and path[1] in G[path[0]]):
                if len(path) == 3 and len(path) > temp:
                    temp = 3
                if len(path)>3 and len(path) > temp:
                    temp = len(path)+1
                    # print path
    # max_path = max(max_path, key=lambda l: len(l))
    # print max_path
    # print len(all_paths)
    return temp
    # print(all_paths)
    # print("Longest Path:")
    # print(max_path)
    # print("Longest Path Length:")
    # print len(max_path)


# edges = [['1', '3'], ['2', '3'], ['3', '4'], ['4', '3']]

# print longest_path(edges)


file_name = "C-small-practice.in"
with open(file_name, 'r') as f:
    lines = f.read().splitlines()

n = int(lines[0])
for i in xrange(0, n):
# i = 1
    line_1 = lines[1 + i * 2]
    line_2 = lines[2 + i * 2]
    e = line_2.split()
    edges = []
    for j in xrange(0, len(e)):
        edges.append([str(j + 1), str(e[j])])
    # print (edges)
    # print longest_path(edges)
    print("Case #%d: %s" % (i + 1, longest_path(edges)))

#     line_3 = lines[3 + i * 3]
# print("Case #%d: %s" % (i + 1, test_example(line_1, line_2, line_3)))
