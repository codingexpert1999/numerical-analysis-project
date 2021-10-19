import numpy as np

def cholesky(Α):
    Α = np.array(Α, float)
    L = np.zeros_like(Α)

    n,_ = np.shape(Α)

    for j in range(n):
        for i in range(j, n):
            if i == j: 
                L[i, j] = np.sqrt(Α[i, j] - np.sum(L[i, :j]**2))
            else:
                L[i, j] = (Α[i, j] - np.sum(L[i, :j]*L[j, :j])) / L[j, j]
    
    return L

A = [
        [5.2, 3, 0.5, 1, 2],
        [3, 6.3, -2, 4, 0],
        [0.5, -2, 8, -3.1, 3],
        [1, 4, -3.1, 7.6, 2.6],
        [2, 0, 3, 2.6, 15]
    ]

L = cholesky(A)

print(L)
print("Και άμα τον πολλαπλασιάσουμε με τον Lτ τότε θα δούμε ότι θα πάρουμε πίσω τον Α")
print(np.dot(L, np.transpose(L)))