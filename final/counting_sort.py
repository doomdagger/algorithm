
__author__ = "He Li"


def counting_sort(A, k):
    B = [0 for i in range(len(A))]
    C = [0 for i in range(k)]

    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B


a = [9, 8, 8, 6, 5, 2, 1, 1, 0]
print counting_sort(a, 10)
