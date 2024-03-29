import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def f(x, c):
    return x**2 + c


# seeds definitions
params = np.arange(-0.75, 0.25, 1/200)
params = np.concatenate((params, np.arange(-1.25, -0.75, 0.5/200)))
params = np.concatenate((params, np.arange(-1.4, -1.25, 0.15/200)))
params = np.concatenate((params, np.arange(-1.75, -1.4, 0.36/200)))
params = np.concatenate((params, np.arange(-1.78, -1.76, 0.021/200)))
params = np.concatenate((params, np.arange(-2, -1.78, 0.22/200)))

points = []

fig = plt.figure()
axis = fig.add_subplot(111)


iter = 0
cs = []
xs = []

for c in params:
    x = 0
    print(iter, c)
    iter += 1
    total = 1000
    for iteration in range(total):
        x = f(x, c)
        if(abs(iteration-total) < 10):
            cs.append(c)
            xs.append(x)
plt.plot(cs, xs, 'ob')
plt.xlabel('C')
plt.ylabel('X')
plt.show()
