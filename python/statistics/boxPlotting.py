import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
# print(healthcare.head())

# print(healthcare["DRG Definition"].unique())

# '313 - CHEST PAIN' '314 - OTHER CIRCULATORY SYSTEM DIAGNOSES W MCC'
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

# alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]
# costs = alabama_chest_pain[' Average Covered Charges '].values

states = chest_pain['Provider State'].unique()
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

plt.boxplot(datasets, labels = states)
plt.figure(figsize = (20, 6))
plt.show();


'''
What information have you learned by looking at these boxplots side by side? What state has the largest spread? 
What state has the largest median? Which states have the most outliers?

It looks like California, New Jersey, and Florida have the largest spreads. Vermont has almost no spread.

The state with the largest median cost for a chest pain diagnosis is New Jersey. The state with the 
smallest median cost is Maryland.

California, Georgia, and Tennessee all have a fair number of outliers.


Take some time to explore more from here. Here are some ways in which you can investigate the data more:

Look at diagnoses other than '313 - CHEST PAIN'.
Group states by regions. Maybe hospitals in the Northeast charge patients differently than hospitals in the South.
Plot something other than ' Average Covered Charges '. You have data about how much Meidcare pays in the 'Average Medicare Payments' column.
'''