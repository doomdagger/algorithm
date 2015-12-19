
__author__ = "He Li"


def max_heapify(A, i):
    l_i = 2 * i
    r_i = 2 * i + 1

    max_i = i

    if l_i < len(A) and A[l_i] > A[max_i]:
        max_i = l_i
    elif r_i < len(A) and A[r_i] > A[max_i]:
        max_i = r_i

    if max_i is not i:
        temp = A[i]
        A[i] = A[max_i]
        A[max_i] = temp
        max_heapify(A, max_i)


def build_heap(A):
    heap_size = len(A) - 1
    for i in range(heap_size / 2, 0, -1):
        max_heapify(A, i)


