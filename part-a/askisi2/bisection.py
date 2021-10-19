import numpy as np
import random

def f(x):
    return 94*(np.cos(x)**3) - 24*np.cos(x) + 177*(np.sin(x)**2) - 108*(np.sin(x)**4) - 72*(np.cos(x)**3)*(np.sin(x)**2) - 65

def getNewBounds():
    b = random.random() * 3
    a = random.random() * (3 - b)

    return (a, b)

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

def changedBisection(a, b):
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

        a, b = getNewBounds()

        N += 1

    if root == None:
        root = m

    return (keepTheFirstNDecimals(5, root), N)

roots = []
iterations_list = []
for i in range(10):
    root, N = changedBisection(0, 3)

    roots.append(root)
    iterations_list.append(N)

mean_value_root = np.sum(roots) / len(roots)
mean_value_N = np.sum(iterations_list) / len(iterations_list)

root, N = bisection(0, 3)

print(mean_value_root, mean_value_N)
print(root, N)

print(f(mean_value_root))
print(f(root))