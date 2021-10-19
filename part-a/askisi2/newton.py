import numpy as np

def f(x):
    return 94*(np.cos(x)**3) - 24*np.cos(x) + 177*(np.sin(x)**2) - 108*(np.sin(x)**4) - 72*(np.cos(x)**3)*(np.sin(x)**2) - 65

def df(x):
    return np.sin(x)*(
        -282*(np.cos(x)**2) + 24 + 354*np.cos(x) - 432*(np.sin(x)**2)*np.cos(x) + 216*(np.cos(x)**2)*(np.sin(x)**2) + 144*(np.cos(x)**4)*np.sin(x)
    )
def d2f(x):
    return 282*(2*np.cos(x)*(np.sin(x)**2) - np.cos(x)**3) + 24*np.cos(x) + 354*(np.cos(x)**2 - np.sin(x)**2) - 432*(3*(np.sin(x)**2)*np.cos(x) + np.sin(x)**4) - 216*(2*np.cos(x)*(np.sin(x)**4) + 3*(np.cos(x)**3)*(np.sin(x)**2)) - 144*((np.cos(x)**3)*(np.sin(x)**2) + np.cos(x)**5)

def x_star(x):
    return x - (f(x) / df(x))

def x_star_changed(x):
    return x_star(x) - 0.5*(((f(x)**2)*d2f(x)) / df(x)**3) 

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

def newton(x_guess):
    x_current = x_guess
    error_bound = 0.001
    x_new = None
    N = 1
    x_list = []

    while True:
        try:
            x_new = x_star(x_current)
        except ZeroDivisionError:
            print("Local max or local min. f'(x) = 0")
            return (None, None, None)

        if(np.abs(x_current - x_new) <= error_bound) or f(x_new) == 0:
            x_new = keepTheFirstNDecimals(5, x_new)
            convergence = getFixedValues(getConvergeRate(x_list, x_new))
            return (x_new, N, convergence[len(convergence) - 1])

        x_list.append(x_new)
        x_current = x_new
        N += 1

def newton_changed(x_guess):
    x_current = x_guess
    error_bound = 0.001
    x_new = None
    N = 1
    x_list = []

    while True:
        try:
            x_new = x_star_changed(x_current)
        except ZeroDivisionError:
            print("Local max or local min. f'(x) = 0")
            return (None, None, None)

        if(np.abs(x_current - x_new) <= error_bound) or f(x_new) == 0:
            x_new = keepTheFirstNDecimals(5, x_new)
            convergence = getFixedValues(getConvergeRate(x_list, x_new))
            return (x_new, N, convergence[len(convergence) - 1])


        x_list.append(x_new)
        x_current = x_new
        N += 1

results = newton_changed(1.5)

if results[0] != None:
    print("Η ρίζα (ή μια προσέγγιση της είναι) " + str(results[0]) + " η οποία βρέθηκε μετά από "+ str(results[1]) + " αριθμούς επαναλήψεων με σύγκλιση " + str(results[2]))


results = newton_changed(1.8)

if results[0] != None:
    print("Η ρίζα (ή μια προσέγγιση της είναι) " + str(results[0]) + " η οποία βρέθηκε μετά από "+ str(results[1]) + " αριθμούς επαναλήψεων με σύγκλιση " + str(results[2]))

print("Τώρα η μη τροποποιημένη μέθοδος")

results = newton(1.5)

if results[0] != None:
    print("Η ρίζα (ή μια προσέγγιση της είναι) " + str(results[0]) + " η οποία βρέθηκε μετά από "+ str(results[1]) + " αριθμούς επαναλήψεων με σύγκλιση " + str(results[2]))


results = newton(1.8)

if results[0] != None:
    print("Η ρίζα (ή μια προσέγγιση της είναι) " + str(results[0]) + " η οποία βρέθηκε μετά από "+ str(results[1]) + " αριθμούς επαναλήψεων με σύγκλιση " + str(results[2]))