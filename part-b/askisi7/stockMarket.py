import numpy as np
import matplotlib.pyplot as plt

# First stock
x_1 = [3, 4, 5, 6, 7, 10, 11, 12, 13, 14] # Cener 3/8/2020 έως 14/8/2020
y_1 = [0.93, 0.944, 0.95, 0.947, 0.924, 0.876, 0.915, 0.934, 0.931, 0.94]

x_1_next = [17, 18, 19, 20, 21, 24]
y_1_next = [0.938, 0.92, 0.93, 0.932, 0.931, 0.913]

# Second stock
x_2 = [3, 4, 5, 6, 7, 10, 11, 12, 13, 14] # TITC 3/8/2020 έως 14/8/2020
y_2 = [11.3, 11.26, 11.42, 11.4, 11.24, 11.2, 11.2, 11.26, 11.34, 11.3]

x_2_next = [17, 18, 19, 20, 21, 24]
y_2_next = [11.3, 11.4, 11.34, 11.22, 11.18, 11.2]

# Θα λύσω για χ από 17 έως 24
# 2 degree polynomial -> a + bx + cx^2
# 3 degree polynomial -> a + bx + cx^2 + dx^3
# 4 degree polynomial -> a + bx + cx^2 + dx^3 + kx^4

def plotPolynomial(x, y, coeffs, title):
    points = len(x)

    # Stock Values Scatter Plot
    for i in range(points - 1):
        plt.scatter(x[i], y[i], c='blue', marker='o', s=50)

    # Polynomial Graph
    y_regression = [computePolynomialForX(coeffs, xi) for xi in x]
    plt.plot(x, y_regression, 'g-')

    # Actual Closing Price in day n (last element of x)
    plt.scatter(x[points - 1], y[points - 1], c='orange', marker='o', s=75)

    # New estimated closing price using the polynomial
    plt.scatter(x[points - 1], y_regression[points - 1], c='red', marker='o', s=75)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(linestyle="dotted")
    plt.title(title)
    plt.show()

def computePolynomialForX(coeffs, x):
    return np.sum([coeffs[i]*(x**i) for i in range(len(coeffs))])

def getXMatrix(x, degree):
    X = []
    n = len(x)

    for i in range(n):
        row = []
        for j in range(degree + 1):
            row.append(x[i]**j)
        X.append(row)

    return np.array(X)

def polynomialRegression(x, y, degree):
    X = getXMatrix(x, degree)

    coeffs = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)), np.transpose(X)), y) # (X_transpose*X)^-1 * X_transpose * y

    return coeffs

def CenerStocks():
    global x_1, y_1, x_1_next
    for day, value in zip(x_1_next, y_1_next):
        degree = 2 # Change this to compute different degrees
        x_1 = np.append(x_1, day)
        y_1 = np.append(y_1, value)

        coeffs = polynomialRegression(x_1, y_1, degree)
        plotPolynomial(x_1, y_1, coeffs, "Cener market values")

def TitcStocks():
    global x_2, y_2, x_2_next
    for day, value in zip(x_2_next, y_2_next):
        degree = 2 # Change this to compute different degrees
        x_2 = np.append(x_2, day)
        y_2 = np.append(y_2, value)

        coeffs = polynomialRegression(x_2, y_2, degree)
        plotPolynomial(x_2, y_2, coeffs, "TITC market values")

  
TitcStocks()

# Uncomment this function
# CenerStocks()