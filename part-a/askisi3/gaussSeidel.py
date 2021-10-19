import numpy as np

def keepTheFirstNDecimals(n, num):
    if len(str(num).split(".")) == 1 or len(str(num).split(".")[1]) <= n:
        return num
    else:
        before_decimal = str(num).split(".")[0]
        after_decimal = str(num).split(".")[1]
        return np.float(before_decimal + "." + after_decimal[0:n])

def makeMatrix(n):
    A = []
    b = []

    for i in range(n):
        rowA = []
        for j in range(n):
            if i == j:
                rowA.append(5)
            else:
                rowA.append(-2)
        A.append(rowA)
        if i == 0 or i == n-1:
            b.append(3)
        else:
            b.append(1)

    return (A, b)

def gaussSeidel(A, b):
    error_bound = 0.005
    n = len(b)
    x = np.zeros_like(b, float)
    prev_x = np.copy(x)
    loops = 1

    while loops < 50:
        for i in range(n):
            sum_x = 0

            for j in range(n):
                if i != j:
                    sum_x = sum_x + (A[i, j] * x[j])

            x[i] = keepTheFirstNDecimals(4, (b[i] - sum_x) / A[i, i])

        if np.abs(np.sum(x) - np.sum(prev_x)) <= error_bound:
            break
        
        prev_x = np.copy(x)
        loops += 1
    
    print("Οι προσεγγίσεις των λύσεων είναι: ")
    print(x)
    print("Επαναλήψεις που έγιναν: ", loops)

A,b = makeMatrix(10)
# A,b = makeMatrix(1000)

A = np.array(A, float)
b = np.array(b, float)

gaussSeidel(A, b)
