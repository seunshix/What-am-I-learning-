
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
# print(data.head())

life_expectancy = data['Life Expectancy']

life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
print(life_expectancy_quartiles)

plt.hist(life_expectancy)
plt.show();

gdp = data['GDP']
median_gdp = np.median(gdp)
print(median_gdp)

low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [0.25, 0.5, 0.75])
print(low_gdp_quartiles, high_gdp_quartiles)

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()

'''
Once again, consider a country that has a life expectancy of 70 years. 
If that country is in the top half of GDP countries, is it in the first, 
second, third, or fourth quarter of the data with respect to life 
expectancy? What if the country is in the bottom half of GDP countries? 

70 is below the first quartile of the high GDP dataset, so it falls in 
the first quarter of that dataset. 70 is between the second and third 
quartile of the low GDP dataset, so it falls in the third quarter.
'''