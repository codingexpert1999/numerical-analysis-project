import numpy as np
import matplotlib.pyplot as plt

def plotSlope(m, b, x, y):
    for i in range(len(x)):
        plt.scatter(x[i], y[i], c='orange', marker='o', s=80)

    slope = m * x + b

    error = y - slope

    plt.plot(x, slope, label="least squares")
    plt.plot(x, error, label="error")
    plt.title("Least Squares")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid(linestyle="dotted")
    plt.legend(loc="upper left")
    plt.show()

def leastSquares(theta):
    x = np.array([-np.pi, -3, -2.97, 3.1, 1.3, 0, -1.3, np.pi, 3, 1.5], np.float)

    x = np.append(x, theta)
    x.sort()

    y = np.sin(x)
    xy = x * y
    x_square = x**2

    n = len(x)

    m = (n * np.sum(xy) - np.sum(x)*np.sum(y)) / (n * np.sum(x_square) - np.sum(x)**2)
    b = (np.sum(y) - m * np.sum(x)) / n

    plotSlope(m, b, x, y)

while True:
    theta = float(input("Enter an angle in degrees (-pi, pi): "))
    theta = np.deg2rad(theta)

    if theta >= -np.pi and theta <= np.pi:
        break

leastSquares(theta)
