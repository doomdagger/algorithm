import math


def new_new_k_quantiles(items, p, q, k, l):
    if k == 1:
        return
    if p > q:
        return

    n = q - p + 1

    if n / k < 1:
        print "error"
        return

    i = k / 2
    x = select(items[p:q+1], i * n / k)
    partition(items[p:q+1], x)

    index = int(i * n / k)
    new_new_k_quantiles(items, p, index, k / 2, l)
    l.append(x)
    new_new_k_quantiles(items, index+1, q, int(math.ceil(k / 2.0)), l)


def new_k_quantiles(items, k, l):
    if k != 1:
        n = len(items)
        i = k / 2
        x = select(items, i * n / k)
        partition(items, x)

        index = int(i * n / k)
        new_k_quantiles(items[:index], k / 2, l)
        l.append(x)
        new_k_quantiles(items[index + 1:], int(math.ceil(k / 2.0)), l)


def k_quantiles(items, k):
    index = median_index(len(items))

    if k == 1:
        return []
    elif k % 2:
        n = len(items)
        left_index = math.ceil((k // 2) * (n / k)) - 1
        right_index = n - left_index - 1

        left = select(items, left_index)
        right = select(items, right_index)

        partition(items, left)
        lower = k_quantiles(items[:left], k // 2)
        partition(items, right)
        upper = k_quantiles(items[right + 1:], k // 2)

        return lower + [left, right] + upper
    else:
        index = median_index(len(items))
        median = select(items, index)
        partition(items, median)

        return k_quantiles(items[:index], k // 2) + \
               [median] + \
               k_quantiles(items[index + 1:], k // 2)


def median_index(n):
    if n % 2:
        return n // 2
    else:
        return n // 2 - 1


def partition(items, element):
    i = 0

    for j in range(len(items) - 1):
        if items[j] == element:
            items[j], items[-1] = items[-1], items[j]

        if items[j] < element:
            items[i], items[j] = items[j], items[i]
            i += 1

    items[i], items[-1] = items[-1], items[i]

    return i


def select(items, n):
    if len(items) <= 1:
        return items[0]

    medians = []

    for i in range(0, len(items), 5):
        group = sorted(items[i:i + 5])
        items[i:i + 5] = group
        median = group[median_index(len(group))]
        medians.append(median)

    pivot = select(medians, median_index(len(medians)))
    index = partition(items, pivot)

    if n == index:
        return items[index]
    elif n < index:
        return select(items[:index], n)
    else:
        return select(items[index + 1:], n - index - 1)


# [1, 2, 4, 5, 7, 7, 8, 12, 17, 19]
value = [0, 1, 2,3]
k = 3

temp = []
new_new_k_quantiles(value, 1, len(value)-1, k, temp)

print(temp)
value = [1, 2,3]
temp = []
new_k_quantiles(value, k, temp)

print(temp)

#temp = k_quantiles(value, k)

#print(temp)


