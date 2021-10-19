import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 94*(np.cos(x)**3) - 24*np.cos(x) + 177*(np.sin(x)**2) - 108*(np.sin(x)**4) - 72*(np.cos(x)**3)*(np.sin(x)**2) - 65

xValues = []
yValues = []

for x in np.arange(0, 3, 0.01):
    xValues.append(x)
    yValues.append(f(x))

plt.plot(xValues, yValues)
plt.grid()
plt.xlabel("x values")
plt.ylabel("f(x) values")
plt.show()