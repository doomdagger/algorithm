import copy

__author__ = 'lihe'


def floyd_warshall(G):
    rows_num = len(G)
    D = copy.deepcopy(G)
    for k in range(rows_num):
        for i in range(rows_num):
            for j in range(rows_num):
                if D[i][k] is not None and D[k][j] is not None:
                    if D[i][j] is None:
                        D[i][j] = D[i][k] + D[k][j]
                    else:
                        D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    return D


def extend_shortest_paths(L, W):
    rows_num = len(L)
    LL = [[None for i in range(rows_num)] for j in range(rows_num)]
    for i in range(rows_num):
        for j in range(rows_num):
            for k in range(rows_num):
                if L[i][k] is not None and W[k][j] is not None:
                    if LL[i][j] is None:
                        LL[i][j] = L[i][k] + W[k][j]
                    else:
                        LL[i][j] = min(LL[i][j], L[i][k] + W[k][j])
    return LL


def another_algorithm(G):
    rows_num = len(G)
    L = copy.deepcopy(G)

    m = 2
    while m < rows_num - 1:
        L = extend_shortest_paths(L, L)
        m *= 2

    return L


g = [
    [0, 3, None, None],
    [None, 0, 12, 5],
    [4, None, 0, -1],
    [2, -4, None, 0]
]
# intentional bad graph, has a negative-weight cycle
# g = [
#     [0, 3, None, None, None],
#     [None, 0, 1, None, None],
#     [None, None, 0, -1, 4],
#     [None, -1, None, 0, None],
#     [None, None, None, None, 0]
# ]
print floyd_warshall(g)
print another_algorithm(g)
