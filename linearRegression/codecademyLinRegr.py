# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())

# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed, codecademy.score)
# Show then clear plot
plt.show() # Show the plot
plt.clf() # Clear the plot

''' from the plot, relationship appears to be linear'''

# Create the model here:
model = sm.OLS.from_formula('score ~ completed', data = codecademy)

# Fit the model here:
results = model.fit()

# Print the coefficients here:
print(results.params)
print()

# Fit a linear regression to predict score based on prior lessons completed
'''
Intercept interpretation:
A student who has completed 0 lessons will have a score of 13
Slope interpretation:
For every additional course completed, score is expected to increase by 1.3
'''
# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)
plt.plot(codecademy.completed, results.predict(codecademy))
# Show then clear plot
plt.show() # Show the plot
plt.clf() # Clear the plot

# Predict score for learner who has completed 20 prior lessons
lessons_completed= {'completed': [20]}
pred = results.predict(lessons_completed)
print(pred)
print()
# Calculate fitted values
fitted_values = results.predict(codecademy)

# Calculate residuals
residuals = codecademy.score - fitted_values

# Check normality assumption
plt.hist(residuals)
# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
# Show then clear the plot
plt.show()
plt.clf()

# Create a boxplot of score vs lesson
sns.boxplot(x = 'lesson', y = 'score', data = codecademy)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', data = codecademy)

result = model.fit()
print(result)

# Calculate and print the group means and mean difference (for comparison)
print(codecademy.groupby('lesson').mean().score)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()

