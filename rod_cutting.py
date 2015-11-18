__author__ = 'lihe'


def rod_cutting(p, n):
    c = [0 for i in range(n+1)]
    s = [0 for i in range(n+1)]

    c[0] = 0

    for i in range(1, n+1):
        c[i] = -9999
        for j in range(len(p)):
            if j+1 <= i:
                if c[i-j-1]+p[j] > c[i]:
                    c[i] = c[i-j-1]+p[j]
                    s[i] = j+1

    return c, s


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
c, s = rod_cutting(p, 4)

print c
print s