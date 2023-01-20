import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for column in columns:
  # print(column)
  sns.countplot(df[column],  order=df[column].value_counts().index)
  # rotates the value labels slightly so they don’t overlap, also slightly increases font size
  plt.xticks(rotation=30, fontsize=10)
  # increases the variable label font size slightly to increase readability
  plt.xlabel(column, fontsize=12)
  plt.title(f'{column} Value Counts')
  plt.show()
  plt.clf()



'''

Feel free to play around with the graphs and customize them any way you want to help in your analysis! 
Here are some ideas to get yourself started:

Turn any bar graph with less than six bars into a pie chart (hint: use a conditional statement!).
Create your bar charts using a list comprehension instead of a for loop.
Change the color theme of your graphs using the seaborn color or palette parameters.
Remove any graphs you find uninformative.
Change around the current title or label formatting.
Happy Coding! :)
'''

# Scatter plots and co-variance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import pearsonr
np.set_printoptions(suppress=True, precision = 1) 

penguins = pd.read_csv('penguins.csv')

print(penguins.head())
plt.scatter(penguins.flipper_length_mm, penguins.body_mass_g)
plt.show()

cov, p = pearsonr(penguins.flipper_length_mm, penguins.body_mass_g)
print(cov)

