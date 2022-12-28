import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# fig1, ax = plt.subplots() # Create a figure containing a single axes
# ax.plot([6, 5.4, 2.6, 2.4, 1.8], [0.8, 1.4,1.6, 4.4, 5]);
# plt.show()


# '''
# A figure keeps track of all the child Axes, a group of special
# Artist(titles, figure, legends, colorbars) and even nested subfigure'''
# fig2 = plt.figure() # an empty picture with no axes
# fig2, ax2 = plt.subplots() # a figure with a single axes
# fig2, axs2 = plt.subplots(3, 3) # a figure with 4x4 grid of axes
# plt.show()


# b = np.matrix([[1,2], [3,4]])
# b_asarray = np.asarray(b)


np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize = (5, 2.7), layout = 'constrained')
ax.scatter('a', 'b', c = 'c', s = 'd', data = data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b');
plt.show()

# Coding styles
# =============
#
# The explicit and the implicit interfaces
# ----------------------------------------
#
# As noted above, there are essentially two ways to use Matplotlib:
#
# - Explicitly create Figures and Axes, and call methods on them (the
#   "object-oriented (OO) style").
# - Rely on pyplot to implicitly create and manage the Figures and Axes, and
#   use pyplot functions for plotting.
#
# See :ref:`api_interfaces` for an explanation of the tradeoffs between the
# implicit and explicit interfaces.
#
# So one can use the OO-style

x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend();  # Add a legend.

###############################################################################
# or the pyplot-style:

x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend();


# Making a helper functions
# -------------------------
#
# If you need to make the same plots over and over again with different data
# sets, or want to easily wrap Matplotlib methods, use the recommended
# signature function below.


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    plt.show()
    return out

###############################################################################
# which you would then use twice to populate two subplots:

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'});
my_plotter(ax2, data3, data4, {'marker': 'o'});

###############################################################################