import numpy as np
import matplotlib.pyplot as plt
import math


def f(x, c, n):
    for i in range(n):
        x = x**3+c*x
    return x


def cero(x, a, b):
    if(a > x < b):
        return True
    return False


# Orbits Calculation
n = 8
x = 0
cs = []
xs = []
params = np.arange(-3, 0, 10**(-5))
for c in params:
    x_0 = math.sqrt(-c/3)
    x = f(x_0, c, 2**n)
    print(c)
    cs.append(c)
    xs.append(abs(x-x_0))

# Period-doubling Bifurcation
ceros = []
for i in range(1, len(xs)-1):
    if(cero(xs[i], xs[i-1], xs[i+1])):
        ceros.append(cs[i])

print(ceros[-n:])

# Feigenbaum Constant
for i in range(n-3):
    print((ceros[-i-1]-ceros[-i-2])/(ceros[-2-i]-ceros[-i-3]))
plt.plot(cs, xs, 'ob')
plt.xlabel('C')
plt.ylabel('X')
plt.show()
