import numpy as np

def f(x):
    return np.exp(np.sin(x)**3) + x**6 - 2*(x**4) - x**3 - 1

def next_x(x, prev_x):
    return x - ((f(x) * (x - prev_x)) / (f(x) - f(prev_x)))

def keepTheFirstNDecimals(n, num):
    if len(str(num).split(".")) == 1 or len(str(num).split(".")[1]) <= n:
        return num
    else:
        before_decimal = str(num).split(".")[0]
        after_decimal = str(num).split(".")[1]
        return np.float(before_decimal + "." + after_decimal[0:n])

def secant(x0_guess, x1_guess):
    x0 = x0_guess
    x1 = x1_guess
    N = 1

    error_bound = 0.001

    while True:
        x_new = next_x(x1, x0)

        if np.abs(x1 - x_new) <= error_bound or f(x_new) == 0:
            return (keepTheFirstNDecimals(5, x_new), N)

        x0 = x1
        x1 = x_new
        N += 1

root, N = secant(-2, -1)

print("H ρίζα (ή μια προσέγγιση της) είναι: " + str(root))
print("Η οποία βρέθηκε μετά από " + str(N) + " αριθμούς επαναλήψεων")

root, N = secant(1, 2)

print("H ρίζα (ή μια προσέγγιση της) είναι: " + str(root))
print("Η οποία βρέθηκε μετά από " + str(N) + " αριθμούς επαναλήψεων")