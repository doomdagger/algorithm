"""
Exercise 22.2-7

"""
from my_util.graph_util import *

__author__ = 'He Li'


def wrestlers(n, r):
    # build a graph
    graph = [[0 for i in range(n)] for j in range(n)]
    for pair in r:
        x = pair[0]
        y = pair[1]
        graph[x][y] = 1
        graph[y][x] = 1

    # 0 stands for white
    # 1 stands for gray
    # 2 stands for black
    inf = 999999
    color = [0] * len(graph)
    d = [inf] * len(graph)
    pi = [None] * len(graph)
    role = [-1] * len(graph)

    color[0] = 1
    d[0] = 0
    role[0] = 0
    queue = [0]

    while len(queue) > 0:
        u = queue.pop(0)
        u_adj = fetch_adjacent(graph, u)
        for adj in u_adj:
            if color[adj] == 0:
                color[adj] = 1
                d[adj] = d[u] + 1
                pi[adj] = u
                if role[u] is 0:
                    role[adj] = 1
                elif role[u] is 1:
                    role[adj] = 0
                else:
                    raise RuntimeError("role[u] is -1?")
                queue.append(adj)
            else:
                if role[adj] == role[u]:
                    print "Same role collision."
                    return False
                elif role[adj] is -1:
                    raise RuntimeError("visited role[adj] is -1?")
        color[u] = 2

    return d, pi, color, role

print wrestlers(10, [[1, 2], [2, 4]])
