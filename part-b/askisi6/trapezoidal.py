import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def trapezoidal(x):
    n = len(x)

    a = x[0]
    b = x[n - 1]
    h = (b - a) / n

    integral = (h/2)*(f(a) + 2*np.sum(x[1:(n - 1)]) + f(b))

    return integral
    

x = np.linspace(0.5, np.pi/2, 11)

integral_f = -np.cos(x[len(x) - 1]) + np.cos(x[0])
print("Integral of f(x) is: " + str(integral_f))

integral_p = trapezoidal(x)
print("Integral using trapezoidal rule is: " + str(integral_p))

error = np.fabs(integral_p - integral_f)

print("error = " + str(error))