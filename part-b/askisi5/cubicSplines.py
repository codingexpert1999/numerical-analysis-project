import numpy as np
import matplotlib.pyplot as plt

def coefficients(yk, hk, yppk):
    ak = yk
    bk = np.array([ (yk[i+1] - yk[i])/hk[i] - (2.*yppk[i] + yppk[i + 1])*hk[i]/6 for i in range(len(hk)) ], np.float)
    ck = yppk * 0.5
    dk = np.array([ (yppk[i + 1] - yppk[i])/(hk[i]*6) for i in range(len(hk)) ], np.float)
    return (ak, bk, ck, dk)

def S(x, a, b, c, d, xk):
    i = 0

    while i < len(xk) - 1 and x >= xk[i]: # find the interval that contains x
        i += 1

    i -= 1
    dx = x - xk[i]
    return a[i] + dx*(b[i] + dx*(c[i] + d[i]*dx)) # Horner's method for computational efficiency: a + x*(b + x*(c + x*d))

def cubicSplines():
    xk = np.array([-np.pi, -3, -2.97, -1.97, -0.32, 0.13, 1.4, 2.1, 2.9, 3.1], np.float)
    yk = np.sin(xk)
    n = len(xk) - 1
    hk = np.array([xk[i + 1] - xk[i] for i in range(n)])

    ypp0 = 0 # natural splines y0'' = 0
    yppn = 0 # natural splines yn'' = 0

    A = np.zeros((n - 1, n - 1))
    b = np.zeros(n - 1)

    for i in range(n - 1):
        A[i, i] = 2 * (hk[i] + hk[i + 1])

        if i > 0 :
            A[i, i - 1] = hk[i]
            
        if i < n - 2:
            A[i, i + 1] = hk[i + 1]

        b[i] = 6 * ( (yk[i + 2] - yk[i + 1]) / hk[i + 1] - (yk[i + 1] - yk[i]) / hk[i] )

    b[0] -= hk[0] * ypp0
    b[-1] -= hk[n - 1]* yppn

    x = np.linalg.solve(A, b)
    ypp = np.insert(x, (0, len(x)), (ypp0, yppn))

    coeffs = coefficients(yk, hk, ypp)

    plotError(coeffs, xk)

def plotError(coeffs, xk):
    x_splines = np.linspace(-np.pi, np.pi, 200)
    a, b, c, d = coeffs

    spline = [S(x,a,b,c,d,xk) for x in x_splines]

    x_sinx = np.linspace(-np.pi, np.pi, 200)
    y_sinx = np.sin(x_sinx)

    plt.title("Cubic spline interpolation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(linestyle="dotted")
    plt.plot(x_splines,spline, label="polynomial")
    plt.plot(x_sinx, y_sinx, label="sin(x)")
    plt.legend(loc="upper center")

    plt.show()

cubicSplines()