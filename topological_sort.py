from depth_first_search import *
from quick_sort import *

__author__ = 'He Li'


def topological_sort(graph):
    color, pi, d, f = depth_first_search(graph)
    f, vertices = quick_sort(f, 0, len(f) - 1, fetch_vertices(graph))
    f.reverse()
    vertices.reverse()
    return f, vertices


# gg = [
#     [0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 1],
#     [0, 0, 0, 0, 0, 1]
# ]
#
# print topological_sort(gg)
