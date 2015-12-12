__author__ = 'He Li'


def quick_sort(array, p, r, order=None):
    if p < r:
        q = partition(array, p, r, order)
        quick_sort(array, p, q - 1, order)
        quick_sort(array, q + 1, r, order)

    return array, order


def partition(array, p, r, order):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

            # record order
            if order is not None:
                temp = order[i]
                order[i] = order[j]
                order[j] = temp

    array[r] = array[i + 1]
    array[i + 1] = x

    # record order
    if order is not None:
        temp = order[r]
        order[r] = order[i + 1]
        order[i + 1] = temp

    return i + 1

# print quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 8)
