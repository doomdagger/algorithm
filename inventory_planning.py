__author__ = 'lihe'


def InventoryPlanning(L):
    n = len(L)

    for i in range(1, n):
        L[i] = L[i] + L[i-1]

    c = [[100 for i in range(L[n-1]+1)] for i in range(n)]
    b = [[100 for i in range(L[n-1]+1)] for i in range(n)]

    c[0][0] = 0

    for j in range(L[1], L[n-1]+1):
        c[1][j] = c[0][0]+5*max(0, j-0-10)+h(j-L[1])
        b[1][j] = 0

    for i in range(2, n):
        for j in range(L[i], L[n-1]+1):
            c[i][j] = 1000000

            for k in range(L[i-1], j+1):
                temp = c[i-1][k]+5*max(0, j-k-10)+h(j-L[i])
                if temp < c[i][j]:
                    c[i][j] = temp
                    b[i][j] = k

    # print b[n-1][L[n-1]]
    return c, b


def h(j):
    return j*0.5


def PrintPlan(L, c, b, i, j):
    if i < 1:
        return
    else:
        print "D(i):" + str(L[i]) + "\t\tj:" + str(j) + "\tk:" + str(b[i][j]) + "\tc:" + str(c[i][j])
        PrintPlan(L, c, b, i-1, b[i][j])


L = [0, 20, 10, 15, 10, 22, 30, 1, 5, 15]
c, b = InventoryPlanning(L)
PrintPlan(L, c, b, len(L)-1, L[-1])
