import pandas as pd
import numpy as np

car_eval = pd.read_csv('python\statistics\car_eval_dataset.csv')
print(car_eval.head())

print(car_eval.columns)
print('-' * 50)

# Summarizing Manufacturing Country
print(car_eval['manufacturer_country'].value_counts())
# United states appears to be the 4th
print(car_eval['manufacturer_country'].value_counts(normalize = True, dropna = True))
# Japan appears to be 22.8% for percentage of cars
print('-' * 50)

# Summarizing Buying Costs
print(car_eval['buying_cost'].unique())
cost_order = ['low', 'med', 'high', 'vhigh']
car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], cost_order, ordered = True)
print('-' * 50)

# Calculate median category of buying_cost
cost_median = np.median(car_eval['buying_cost'].cat.codes)
print(cost_median)

cost_median_cat = cost_order[int(cost_median)]
print(cost_median_cat)

print('-' * 50)

# Summarizing Luggage Capacity

print(car_eval['luggage'].value_counts(normalize = True))

# checking if there are missing values
print(car_eval['luggage'].value_counts(normalize = True, dropna = False))
# OR
print(car_eval['luggage'].value_counts()/len(car_eval['luggage']))

print('-' * 50)

# Summarizing Passenger Capacity

# print(car_eval['doors'].unique())

# Sum and proportion of cars having more than 5 doors
print((car_eval['doors'] == '5more').sum())
print((car_eval['doors'] == '5more').mean())