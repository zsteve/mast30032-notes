# plot a bifurcation plot for the discrete logistic equation
# described by the map f(x) = r*x*(1-x)

import matplotlib as mp
import matplotlib.pyplot as plt
from task3 import iterate
import numpy as np

x0 = 0.1
round_prec = 5
points = 1000

# finding attracting fixed points by iterating for 2000 cycles, taking last 500
# iterates and then binning values

plt.figure()

r_values = np.linspace(0, 4, num = points)

for r in r_values:
    stable_points = set([])
    
    v = iterate(2000, lambda x: r*x*(1-x), x0 = x0)
    t = v[-500:]
    t = [round(i[1], round_prec) for i in t]

    for i in t:
        stable_points.add(i)
    
    plt.scatter([r, ]*len(stable_points), list(stable_points), s = 1)
    
plt.show()