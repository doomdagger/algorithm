from my_util.graph_util import *

__author__ = 'He Li'

"""
Can modify depth first search to add parenthesis theorem

"""


def depth_first_search(graph):
    # 0 stands for white
    # 1 stands for gray
    # 2 stands for black
    color = [0] * len(graph)
    pi = [None] * len(graph)
    d = [0] * len(graph)
    f = [0] * len(graph)

    time = 0

    vertices = fetch_vertices(graph)
    for vertex in vertices:
        if color[vertex] == 0:
            time = depth_visit(graph, vertex, color, pi, d, f, time)

    return color, pi, d, f


def depth_visit(graph, u, color, pi, d, f, time):
    color[u] = 1
    time += 1
    d[u] = time
    u_adj = fetch_adjacent(graph, u)
    for adj in u_adj:
        if color[adj] == 0:
            pi[adj] = u
            time = depth_visit(graph, adj, color, pi, d, f, time)

    time += 1
    f[u] = time
    color[u] = 2
    return time


# gg = [
#     [0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 1],
#     [0, 0, 0, 0, 0, 1]
# ]
# print depth_first_search(gg)
