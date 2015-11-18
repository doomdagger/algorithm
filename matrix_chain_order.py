# Dynamic Programming Python implementation of Matrix Chain Multiplication
# See the Cormen book for details of the following algorithm
import sys
 
# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one extra column are
    # allocated in m[][].  0th row and 0th column of m[][] are not used
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
 
    # m[i,j] = Minimum number of scalar multiplications needed to compute
    # the matrix A[i]A[i+1]...A[j] = A[i..j] where dimention of A[i] is
    # p[i-1] x p[i]
 
    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0
 
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxint
            for k in range(i, j):
 
                # q = cost/scalar multiplications
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
 
    return (m, s)
 
# Driver program to test above function
arr = [5, 10, 3 ,12, 5, 50, 6]
size = len(arr)

m, s = MatrixChainOrder(arr, size);
 
print m
print s

def PrintOptimalParens(s, i, j):
    if i==j:
        print "A"+str(i)
    else:
        print "(";
        PrintOptimalParens(s, i, s[i][j]);
        PrintOptimalParens(s, s[i][j] + 1, j);
        print ")";

PrintOptimalParens(s, 1, 6); 

# This Code is contributed by Bhavya Jain
