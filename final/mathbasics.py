
__author__ = "He Li"


def merge_sort(A, p, r):
    if p < r - 1:
        q = (r - p) / 2 + p
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    L = [A[i] for i in range(p, q)]
    R = [A[i] for i in range(q, r)]
    L.append(99999)
    R.append(99999)

    l_i = 0
    r_i = 0
    for i in range(p, r):
        if L[l_i] < R[r_i]:
            A[i] = L[l_i]
            l_i += 1
        else:
            A[i] = R[r_i]
            r_i += 1


a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
merge_sort(a, 0, len(a))
print a
