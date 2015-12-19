
___author__ = "He Li"


def matrix_multiplication(a, b):
    row = len(a)
    col = len(b[0])

    c = [[0 for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    return c


a = [
    [3, 1, 1],
    [2, 0, 3]
]

b = [
    [1, 6],
    [2, 0],
    [1, 2]
]

print matrix_multiplication(a, b)