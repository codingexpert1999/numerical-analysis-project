import numpy as np

A = np.array([
        [0, 7, -1, 3, 1],
        [0, 3, 4, 1, 7],
        [6, 2, 0, 2, -1],
        [2, 1, 2, 0, 2],
        [3, 4, 1, -2, 1]
    ], float)

b = np.array([5, 7, 2, 3, 4], float)

def correctPivots(A, b):
    n = len(b) # Matrix size

    for k in range(n-1):
        if np.fabs(A[k, k]) < 1.0e-10:
            for i in range(k+1, n):
                if np.fabs(A[i, k]) > np.fabs(A[k, k]):
                    A[[k, i]] = A[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break

    return A

def gauss(A, b):
    n = len(b) # Matrix size

    A = correctPivots(A, b)

    for k in range(n-1):
        for i in range(k+1, n):
            if A[i, k] == 0: continue

            factor = A[k, k] / A[i, k]

            for j in range(k, n):
                A[i, j] = A[k, j] - A[i, j]*factor
            
            b[i] = b[k] - b[i]*factor

    # Initialize our x variables
    x = np.zeros(n, float)

    # Back-substitution
    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i, j]*x[j]
        x[i] = (b[i] - sum_ax) / A[i, i] 

    return x

print("This matrix solution is : ")
print(gauss(A, b))