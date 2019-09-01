import matplotlib.pyplot as plt
import math

points = []
x = 3.6
iterations = 7
for iteration in range(iterations):
    points.append(x)
    x = math.cos(x)

fig = plt.figure()
axis = fig.add_subplot(111)
axis.plot(range(iterations), points, 'ob')
plt.xlabel('Iteration')
plt.ylabel('Cos(x)')
axis.set_title('Orbit of Cos(x) with seed x=3.6')
plt.savefig('cos.png')
