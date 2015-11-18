__author__ = 'lihe'


def BreakString(L):
    m = len(L)

    s = [[100 for i in range(m)] for i in range(m)]
    r = [[100 for i in range(m)] for i in range(m-1)]

    for i in range(0, m-1):
        s[i][i+1] = 0

    for l in range(2, m):
        for i in range(0, m-l):
            j = i+l
            s[i][j] = 10000
            for k in range(i+1, j):
                temp = s[i][k] + s[k][j] + L[j] - L[i]
                if temp < s[i][j]:
                    s[i][j] = temp
                    r[i][j] = k

    return s, r


def PrintSequence(r, i, j, L):
    if j - i <= 1:
        return
    else:
        print L[r[i][j]]
        PrintSequence(r, i, r[i][j], L)
        PrintSequence(r, r[i][j], j, L)


L=[0, 2, 6, 8, 10, 12, 18, 20]
s, r = BreakString(L)
print s
PrintSequence(r, 0, 7, L)