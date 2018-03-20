import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.style
mp.style.use('classic')

# general purpose iterator for difference equations
# of the form x(n+1) = f(x(n))

def iterate(nf, f, x0 = 1, n0 = 0):
    x = list([(n0, x0), ])
    assert(nf > n0)
    n = n0+1
    while n <= nf:
        x += [(n, f(x[-1][1])), ]
        n+=1
    return x
    
# example - geometric growth
plt.figure()
plt.subplot(121)
v = iterate(100, lambda x: 1.10*x)
plt.scatter([i[0] for i in v], [i[1] for i in v])

# example - discrete logistic model
# u(t+1) = r*u(t)*(1-u(t))
plt.subplot(122)
v = iterate(100, lambda x: 3.5*x*(1-x), 0.000001)
plt.scatter([i[0] for i in v], [i[1] for i in v])