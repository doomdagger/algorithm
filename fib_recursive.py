__author__ = 'He Li'


def fib_dp(n):
    c = [0 for i in range(n+1)]

    c[0] = 0
    c[1] = c[2] = 1
    for i in range(3, n+1):
        c[i] = c[i-1] = c[i-2]

    return c[n]


def fib_memoize(n):
    c = [0 for i in range(n+1)]

    c[0] = 0
    c[1] = c[2] = 1

    for i in range(3, n+1):
        c[i] = -1

    x = fib_look(n, c)
    print c
    return x


def fib_look(n, c):
    if n == 1 or n == 2:
        return 1

    if n == 0:
        return 0

    if c[n] == -1:
        if c[n-1] == -1:
            fib_look(n-1, c)

        if c[n-2] == -1:
            fib_look(n-2, c)

        c[n] = c[n-1] + c[n-2]

    return c[n]


print fib_memoize(10)
