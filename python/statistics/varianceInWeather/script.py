import pandas as pd
import numpy as np
from weather_data import london_data

print(london_data.head())
# print(london_data.columns)

# print(london_data.iloc[100:200])
# print(len(london_data))

temp = london_data['TemperatureC']

average_temp = np.mean(temp)
print(f'The temperature mean in Celcius is {average_temp}')
temperature_var = np.var(temp)
print(f'The temperature variance is {temperature_var}')
temperature_standard_deviation = np.std(temp)
print(f'The temperature standard deviation is {temperature_standard_deviation}')

june = london_data.loc[london_data['month'] == 6]['TemperatureC']
# print(june)
july = london_data.loc[london_data['month'] == 7]['TemperatureC']
# print(july)

# june_mean = np.mean(june)
# print(f'The average temperature for the month of june is {june_mean}')
# july_mean = np.mean(july)
# print(f'The average temperature for the month of july is {july_mean}')
# june_stdev = np.std(june)
# print(f'The standard deviation for the month of june is {june_stdev}')
# july_stdev = np.std(july)
# print(f'The standard deviation for the month of july is {july_stdev}')
print('*' * 50)
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print(f'The average temperature for the {i} month is {np.mean(month)}')
  print(f'The standard deviation for the {i} month is {np.std(month)} \n')
