import pandas as pd


# Functions Definitions
def F(x):
    return x**2 - 2


def G(x):
    return x**2 - 2.0001


def D(x):
    return (2*x) % 1


# Dict with functions
function = {'F': F, 'G': G, 'D': D}


# Main script
seeds = pd.read_csv('seeds.csv')
columns = list(seeds)
for column in columns:
    orbit = pd.DataFrame(columns=seeds[column])
    for seed in seeds[column]:
        this_orbit = [seed]
        for iteration in range(99):
            this_orbit.append(function[column](this_orbit[-1]))
        orbit[seed] = pd.Series(this_orbit).values
    orbit.to_csv(column+'.csv')
