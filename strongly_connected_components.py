from topological_sort import *

__author__ = 'He Li'


def strongly_connected_components(graph):
    f, order = topological_sort(graph)
    t_graph = [[graph[i][j] for i in range(len(graph[0]))] for j in range(len(graph))]
    color, pi, d, f = modified_depth_first_search(t_graph, order)

    return color, pi, d, f


def modified_depth_first_search(graph, order):
    # 0 stands for white
    # 1 stands for gray
    # 2 stands for black
    color = [0] * len(graph)
    pi = [None] * len(graph)
    d = [0] * len(graph)
    f = [0] * len(graph)

    time = 0

    for vertex in order:
        if color[vertex] == 0:
            time = depth_visit(graph, vertex, color, pi, d, f, time)

    return color, pi, d, f

gg = [
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0]
]
print strongly_connected_components(gg)
