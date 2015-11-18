def new_two_array_median(a, i, j, b, p, q):
    print a[i:j+1], b[p:q+1]
    if j - i + 1 == 1:
        return min(a[i], b[p])

    m = (j - i + 2) // 2
    print i, j, p, q
    print m
    if a[i+m-1] < b[p+m-1]:
        return new_two_array_median(a, j-m+1, j, b, p, p+m-1)
    else:
        return new_two_array_median(a, i, i+m-1, b, q-m+1, q)


def two_array_median(a, b):
    print a, b
    if len(a) == 1:
        return min(a[0], b[0])

    m = median_index(len(a))

    print m

    i = m + 1
    if a[m] < b[m]:
        return two_array_median(a[-i:], b[:i])
    else:
        return two_array_median(a[:i], b[-i:])


def median_index(n):
    if n % 2 == 0:
        return n // 2 - 1
    else:
        return n // 2


# y = [1, 2, 3, 4, 5]
# x = [5, 6, 7, 8, 9]
# print(two_array_median(x, y))
y = [0, 1, 2, 3, 4]
x = [0, 5, 6, 7, 8]
print(new_two_array_median(x, 1, len(x)-1, y, 1, len(y)-1))
