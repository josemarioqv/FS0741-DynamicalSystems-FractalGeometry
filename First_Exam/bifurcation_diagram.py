import numpy as np
import matplotlib.pyplot as plt


def s(x, c):
    return x**3 + c*x


# seeds definitions
params = np.arange(-3, 0.25, 1/20000)


fig = plt.figure()
axis = fig.add_subplot(111)


iter = 0
cs = []
xs = []

for c in params:
    x = 0.1
    print(iter, c)
    iter += 1
    for iteration in range(1000):
        x = s(x, c)
        if(abs(iteration-1000) < 10):
            cs.append(c)
            xs.append(x)
plt.plot(cs, xs, 'ob')
plt.xlabel('C')
plt.ylabel('X')
plt.show()
