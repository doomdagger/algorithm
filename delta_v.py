"""
Exercise 24.1-5

"""


def delta_v(graph, s):
    d = [0] * len(graph)
    pi = [None] * len(graph)

    for k in range(0, len(graph) - 1):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] is not None:
                    if d[j] > d[i] + graph[i][j]:
                        d[j] = d[i] + graph[i][j]
                        pi[j] = i

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] is not None:
                if d[j] > d[i] + graph[i][j]:
                    return False

    return d, pi


gg = [
    [None, -1, -1, None, None],
    [None, None, 2, 6, None],
    [None, 1, None, 4, -1],
    [None, None, None, None, 2],
    [3, None, None, 7, None]
]
print delta_v(gg, 0)
