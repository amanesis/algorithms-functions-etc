// Algorithm to compute matrix exponentiation recursively in Python
// O(logn) complexity for small inputs
// Alternatives: Fibo algo


def MatrixMult(a, b):
    c = []
    for i in range(len(a)):
        c.append([0]*len(b[0]))
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += (a[i][k]*b[k][j])
    return c

def MatrixPower(a, n):
    if n<=0:
        return None
    if n==1:
        return a
    if n==2:
        return MatrixMult(a, a)
    t1 = MatrixPower(a, n/2)
    if n%2 == 0:
        return MatrixMult(t1, t1)
    return MatrixMult(t1, MatrixMult(a, t1))