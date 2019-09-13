import math


# Functions Definitions
def F(x):
    return x**2 + 0.25


def G(x):
    return x**2


def D(x):
    return 1.6*x*(1-x)


def J(x):
    return 0.4*math.sin(x)


# Dict with functions and fixed points
function = {'F': F, 'G': G, 'D': D, 'J': J}
x_o = {'F': 0.5, 'G': 0, 'D': 0.375, 'J': 0}

# Results
iteration = {'F': 0, 'G': 0, 'D': 0, 'J': 0}

# Main script
for f in function:
    x = 0.2
    while(abs(x-x_o[f]) > 10**(-6)):
        x = function[f](x)
        iteration[f] += 1

print(iteration)
