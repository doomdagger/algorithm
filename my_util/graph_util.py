__author__ = 'lihe'


# input format: graph is a matrix, excludes is a list: means you want to exclude which vertices
def fetch_vertices(graph, excludes=()):
    return [i for i in range(len(graph)) if i not in excludes]


# input format: graph is a matrix, u is a vertex
def fetch_adjacent(graph, u):
    return [i for i in range(len(graph[u])) if graph[u][i] != 0]


# graph = [
#     [0, -1, 5, -1, 10],
#     [-1, 0, -1, 4, -1],
#     [-1, 7, 0, 2, 3],
#     [7, 6, -1, 0, -1],
#     [-1, 1, 2, -1, 0]
# ]
# print fetch_adjacent(graph, 2)
# print fetch_vertices(graph, excludes=(0, 2))
