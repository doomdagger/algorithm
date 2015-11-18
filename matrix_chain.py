__author__ = 'lihe'


def matrix_chain(p):
    m = len(p)
    c = [[0 for i in range(m)] for i in range(m)]
    s = [[0 for i in range(m)] for i in range(m)]

    for i in range(m):
        c[0][i] = 0
        c[i][0] = 0
        c[i][i] = 0

    for l in range(2, m):
        for i in range(1, m-l+1):
            j = i + l - 1
            c[i][j] = 100000000000
            for k in range(i, j):
                temp = c[i][k] + c[k+1][j] + p[i-1]*p[k]*p[j]
                if temp < c[i][j]:
                    c[i][j] = temp
                    s[i][j] = k

    return c, s


p = [10, 100, 5, 50, 1]
c, s = matrix_chain(p)

print c[1][len(p)-1]
print c
print s