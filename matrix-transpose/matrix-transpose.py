import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    s=np.shape(A)
    m=(s[1],s[0])
    T = np.zeros(m)
    x=0
    for i in A:
        y=0
        for j in i:
            T[y][x]=j
            y+=1
        x+=1
    return T