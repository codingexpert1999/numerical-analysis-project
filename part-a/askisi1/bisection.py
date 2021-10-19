import numpy as np

def f(x):
    return np.exp(np.sin(x)**3) + x**6 - 2*(x**4) - x**3 - 1

def keepTheFirstNDecimals(n, num):
    if len(str(num).split(".")) == 1 or len(str(num).split(".")[1]) <= n:
        return num
    else:
        before_decimal = str(num).split(".")[0]
        after_decimal = str(num).split(".")[1]
        return np.float(before_decimal + "." + after_decimal[0:n])

def bisection(a, b):
    m = None
    N = 1

    error_bound = 0.001

    root = None

    while (b - a) / 2**N > error_bound:
        m = (a + b) / 2
        fm = f(m)

        if fm == 0:
            root = m
            break

        if fm * f(a) < 0:
            b = m
        else:
            a = m

        N += 1

    if root == None:
        root = m

    return (keepTheFirstNDecimals(5, root), N)

root, N = bisection(-2, 2)
print("H ρίζα (ή μια προσέγγιση της) είναι: " + str(root))
print("Η οποία βρέθηκε μετά από " + str(N) + " αριθμούς επαναλήψεων")