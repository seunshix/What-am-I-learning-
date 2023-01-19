import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("python\statistics\census.py"), delimiter=",")
flights = np.loadtxt(open("python\statistics\flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)
plt.hist(flights, range = (0, 365), bins = 365)
plt.ylabel('Flights by Day')




#Plot bloom
plt.subplot(212)
plt.hist(in_bloom, range = (0, 365), bins = 365)
plt.title('Flights and Flower Blooms by Day')
plt.xlabel('Day of the Year')
plt.ylabel('Bloom Count')
plt.show();
