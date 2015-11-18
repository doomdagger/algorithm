__author__ = 'lihe'


# find longest common subsequence
def NewNewLcsLength(x, y):
    m = len(x)
    n = len(y)

    row = [0 for i in range(min(m, n)+1)]

    inner_loop = min(m, n)
    outer_loop = max(m, n)

    inner_x = False
    if inner_loop == m:
        inner_x = True

    for i in range(1, outer_loop + 1):
        for j in range(1, inner_loop + 1):

            if inner_x:
                x_last = x[j-1]
                y_last = y[i-1]
            else:
                x_last = x[i-1]
                y_last = y[j-1]

            if x_last == y_last:
                temp = row[j-1] + 1
            elif row[0] >= row[j]:
                temp = row[0]
            else:
                temp = row[j]

            row[j-1] = row[0]
            row[0] = temp
        row[len(row)-1] = row[0]
        row[0] = 0

    return row


# find longest common subsequence
def NewLcsLength(x, y):
    m = len(x)
    n = len(y)

    first_row = [0 for i in range(min(m, n)+1)]
    second_row = [0 for i in range(min(m, n)+1)]

    inner_loop = min(m, n)
    outer_loop = max(m, n)

    inner_x = False
    if inner_loop == m:
        inner_x = True

    for i in range(1, outer_loop + 1):
        for j in range(1, inner_loop + 1):

            if inner_x:
                x_last = x[j-1]
                y_last = y[i-1]
            else:
                x_last = x[i-1]
                y_last = y[j-1]

            if x_last == y_last:
                second_row[j] = first_row[j-1] + 1
            elif first_row[j] >= second_row[j-1]:
                second_row[j] = first_row[j]
            else:
                second_row[j] = second_row[j-1]

        first_row = second_row

    return first_row


# find longest common subsequence
def LcsLength(x, y):
    m = len(x)
    n = len(y)

    c = [[0 for i in range(n + 1)] for i in range(m + 1)]
    b = [[0 for i in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i-1]==y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'lu'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'u'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'l'

    return c, b


x = list('ABCBDAB')
y = list('BDCABA')
c, b = LcsLength(x, y)

print c

c = NewLcsLength(x, y)
print c

c = NewNewLcsLength(y, x)
print c

def PrintLcs(b, x, i, j):
    if i==0 or j==0:
        return
    if b[i][j] == 'lu':
        print x[i - 1]
        PrintLcs(b, x, i-1, j-1)
    elif b[i][j] == 'l':
        PrintLcs(b, x, i, j-1)
    else:
        PrintLcs(b, x, i-1, j)


