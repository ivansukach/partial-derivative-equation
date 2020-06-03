import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm


def approximate_y(_i, _j):
    return (1.-h/(tau*a*sigma))*y[_i-1][_j]+(1.-1./sigma)*y[_i][_j-1]+(1./sigma+h/(tau*a*sigma)-1)*y[_i-1][_j-1]


def initial_condition(_x):
    return _x**2


def boundary_condition(_t):
    return 100*(_t**2)


a = -10
sigma = 1
tau = 0.1
h = 0.1
x_min = 0
x_max = 1
t_min = 0
t_max = 1
size_of_x = math.ceil((x_max-x_min)/h)+1
x = np.linspace(x_min, x_max, size_of_x)
print("x values:", x)
size_of_t = math.ceil((t_max-t_min)/tau)+1
t = np.linspace(t_min, t_max, size_of_t)
print("t values:", t)
y = np.zeros((size_of_x, size_of_t))
for i in range(0, size_of_x):
    y[i][0] = initial_condition(x[i])
for j in range(0, size_of_t):
    y[0][j] = boundary_condition(t[j])
for j in range(1, size_of_t):
    for i in range(1, size_of_x):
        y[i][j] = approximate_y(i, j)
np.set_printoptions(precision=3)
print("y values:", y)

# def makeData ():
#     # GRID production from two arrays
#     x_grid, t_grid = np.meshgrid(x, t)
#     zgrid = z([xgrid, ygrid])
#     return xgrid, ygrid, zgrid
#
#
# xt, yt, zt = makeData()

# Create a new figure.
fig = plt.figure()
# The Axes contains most of the figure elements: Axis, Tick, Line2D, Text, Polygon, etc., and sets the coordinate system.
ax = plt.axes(projection='3d')
# Create a surface plot.
ax.plot_surface(x, t, y, cmap=cm.hot)

plt.show()
