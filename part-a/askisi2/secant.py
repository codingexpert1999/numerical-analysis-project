import numpy as np

def f(x):
    return 94*(np.cos(x)**3) - 24*np.cos(x) + 177*(np.sin(x)**2) - 108*(np.sin(x)**4) - 72*(np.cos(x)**3)*(np.sin(x)**2) - 65

def next_x(x, prev_x):
    return x - ((f(x) * (x - prev_x)) / (f(x) - f(prev_x)))

def helper_func(x1, x2):
    return f(x1) / f(x2)

def next_x_changed(x, x_n1, x_n2):
    r = helper_func(x_n2, x_n1)
    q = helper_func(x, x_n1)
    s = helper_func(x_n2, x)
    
    return x_n2 - ((r*(r - q)*(x_n2 - x_n1)) + (1 - r)*s*(x_n2 - x)) / ((q - 1) * (r - 1) * (s - 1))

def getFixedValues(arr):
    temp = []

    for num in arr:
        temp.append(keepTheFirstNDecimals(5, num))

    return temp

def keepTheFirstNDecimals(n, num):
    if len(str(num).split(".")) == 1 or len(str(num).split(".")[1]) <= n:
        return num
    else:
        before_decimal = str(num).split(".")[0]
        after_decimal = str(num).split(".")[1]
        return np.float(before_decimal + "." + after_decimal[0:n])

def getConvergeRate(x_list, root):
    errors = [np.abs(x - root) for x in x_list]
    q = [np.log(errors[n+1] / errors[n]) / np.log(errors[n] / errors[n-1]) for n in range(1, len(errors)-1, 1)]
    return q

def secant(x0_guess, x1_guess):
    x0 = x0_guess
    x1 = x1_guess
    N = 1
    x_list = []

    error_bound = 0.001

    while True:
        x_new = next_x(x1, x0)

        if np.abs(x1 - x_new) <= error_bound or f(x_new) == 0:
            x_new = keepTheFirstNDecimals(5, x_new)
            convergence = getFixedValues(getConvergeRate(x_list, x_new))
            return (x_new, N, convergence[len(convergence) - 1])

        x0 = x1
        x1 = x_new
        x_list.append(x_new)
        N += 1

def secant_changed(x0_guess, x1_guess, x2_guess):
    x0 = x0_guess
    x1 = x1_guess
    x2 = x2_guess
    N = 1
    x_list = []

    error_bound = 0.001

    while True:
        x_new = next_x_changed(x0, x1, x2)

        if np.abs(x2 - x_new) <= error_bound or f(x_new) == 0:
            x_new = keepTheFirstNDecimals(5, x_new)
            convergence = getFixedValues(getConvergeRate(x_list, x_new))
            return (x_new, N, convergence[len(convergence) - 1])

        x0 = x1
        x1 = x2
        x2 = x_new
        x_list.append(x_new)
        N += 1

results = secant_changed(1.5, 1.8, 2)
print("Η ρίζα (ή μια προσέγγιση της είναι) " + str(results[0]) + " η οποία βρέθηκε μετά από "+ str(results[1]) + " αριθμούς επαναλήψεων με σύγκλιση " + str(results[2]))
results = secant_changed(.7, 1.98, 2.4)
print("Η ρίζα (ή μια προσέγγιση της είναι) " + str(results[0]) + " η οποία βρέθηκε μετά από "+ str(results[1]) + " αριθμούς επαναλήψεων με σύγκλιση " + str(results[2]))

print("Τώρα η μη τροποποιημένη μέθοδος")
results = secant(1.5, 2)
print("Η ρίζα (ή μια προσέγγιση της είναι) " + str(results[0]) + " η οποία βρέθηκε μετά από "+ str(results[1]) + " αριθμούς επαναλήψεων με σύγκλιση " + str(results[2]))

results = secant(.7, 2.4)
print("Η ρίζα (ή μια προσέγγιση της είναι) " + str(results[0]) + " η οποία βρέθηκε μετά από "+ str(results[1]) + " αριθμούς επαναλήψεων με σύγκλιση " + str(results[2]))