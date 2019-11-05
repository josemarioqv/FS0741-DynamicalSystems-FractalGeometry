import numpy as np
import matplotlib.pyplot as plt


def f(x, c, n):
    for i in range(n):
        x = x**2+c
    return x


def cero(x, a, b):
    if(a > x < b):
        return True
    return False


n = 8
x = 0
cs = []
xs = []
params = np.arange(-1.5, 0, 10**(-6))
for c in params:
    x = f(0, c, 2**n)
    print(c, x)
    cs.append(c)
    xs.append(abs(x))
ceros = []
for i in range(1, len(xs)-1):
    if(cero(xs[i], xs[i-1], xs[i+1])):
        ceros.append(cs[i])

print(ceros[-n:])
for i in range(n-2):
    print((ceros[-i-1]-ceros[-i-2])/(ceros[-2-i]-ceros[-i-3]))
plt.plot(cs, xs, 'ob')
plt.xlabel('C')
plt.ylabel('X')
plt.show()
