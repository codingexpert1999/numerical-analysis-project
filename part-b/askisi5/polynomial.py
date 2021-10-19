import numpy as np
import matplotlib.pyplot as plt

def plotFunctionWithComputedX(x, y, newX, newY):
    xPoints = np.array([-np.pi, np.pi], np.float)
    xPoints = np.linspace(xPoints[0], xPoints[-1], 200)
    yPoints = np.sin(xPoints)

    plt.scatter(newX, newY, c='green', marker='o', s=80)
    plt.plot(x, y, 'ro', xPoints, yPoints, 'b-')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(linestyle="dotted")
    plt.show()

def plotPolynomialWithError(x, y):
    xPoints = np.linspace(-np.pi, 10*np.pi, 200)
    yPoints = np.sin(xPoints)

    plt.plot(xPoints, yPoints, 'b-', label="sin(x)")
    plt.plot(x, y,'r-', label='polynomial')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.grid(linestyle="dotted")
    plt.legend(loc="upper left")
    plt.show()

def makeInterpolationAndThenShowError(numberOfPoints):
    x = np.linspace(-np.pi, np.pi, numberOfPoints)
    fx = np.sin(x)
    y = []
    n = len(x)

    for xp in x:
        L = np.sum([yi * np.prod((xp - x[x != xi]) / (xi - x[x != xi])) for xi, yi in zip(x, fx)])
    
        y = np.append(y, L)

    plotPolynomialWithError(x, y)


def lagrangeInterpolationForAnX(theta, numberOfPoints):
    x = np.linspace(-np.pi, np.pi, numberOfPoints)

    y = np.sin(x)

    P = 0 # initial polynomial value
    n = len(x) # the degree of the polynomial

    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (theta - x[j]) / (x[i] - x[j])
        P += L * y[i]

    plotFunctionWithComputedX(x, y, theta, P)

def computeXWithPolynomial():
    theta = 0

    while True:
        theta = float(input("Enter an angle in degrees: "))
        theta = np.deg2rad(theta)

        if theta >= -np.pi and theta <= np.pi:
            break
        
    lagrangeInterpolationForAnX(theta, 10)

makeInterpolationAndThenShowError(200)
# computeXWithPolynomial()