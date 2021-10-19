import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(np.sin(x)**3) + x**6 - 2*(x**4) - x**3 - 1

xValues = []
yValues = []

for x in np.arange(-2, 2, 0.01):
    xValues.append(x)
    yValues.append(f(x))

plt.plot(xValues, yValues)
plt.grid()
plt.xlabel("x values")
plt.ylabel("f(x) values")
plt.show()