__author__ = 'lihe'


def integral_knapsack(w, v, b):
    m = len(w)

    c = [[10000 for i in range(b+1)] for i in range(m+1)]
    s = [[10000 for i in range(b+1)] for i in range(m+1)]

    for i in range(m+1):
        c[i][0] = 0

    for i in range(b+1):
        c[0][i] = 0

    for i in range(1, m+1):
        w_o = w[i-1]
        v_o = v[i-1]
        for j in range(1, b+1):
            # TODO finish it after exam
            pass

