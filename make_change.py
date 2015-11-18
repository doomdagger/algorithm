__author__ = 'lihe'


def make_change(n):
    c = [0 for i in range(n+1)]
    s = [0 for i in range(n+1)]

    d = [1, 4, 5, 10]

    c[0] = 0

    for i in range(1, n+1):
        c[i] = 9999
        for k in range(len(d)):
            if d[k] <= i:
                if c[i-d[k]]+1 < c[i]:
                    c[i] = c[i-d[k]]+1
                    s[i] = d[k]

    return c, s


c, s = make_change(8)

print c
print s