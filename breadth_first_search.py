from my_util.graph_util import *

__author__ = 'lihe'


# input format: graph is a matrix, s is the sourch point, which is an integer
def breadth_first_search(graph, s):
    # 0 stands for white
    # 1 stands for gray
    # 2 stands for black
    inf = 999999
    color = [0] * len(graph)
    d = [inf] * len(graph)
    pi = [None] * len(graph)

    color[s] = 1
    d[s] = 0

    queue = [s]

    while len(queue) > 0:
        u = queue.pop(0)
        u_adj = fetch_adjacent(graph, u)
        for adj in u_adj:
            if color[adj] == 0:
                color[adj] = 1
                d[adj] = d[u] + 1
                pi[adj] = u
                queue.append(adj)
        color[u] = 2

    return d, pi, color

gg = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

print breadth_first_search(gg, 2)

