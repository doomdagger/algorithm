__author__ = 'lihe'


def lcs(x, y):
    m = len(x)
    n = len(y)

    c = [[1000 for i in range(n+1)] for i in range(m+1)]
    b = [[1000 for i in range(n+1)] for i in range(m+1)]

    for i in range(n+1):
        c[0][i] = 0

    for i in range(m+1):
        c[i][0] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'lu'
            else:
                if c[i][j-1] <= c[i-1][j]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = 'u'
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = 'l'

    return c, b


