import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
print(census.head())

print(census.dtypes)

census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
print(census['birth_year'].unique())

census['birth_year'] = census['birth_year'].astype('int')
print(census['birth_year'].mean())

census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral',  'agree', 'strongly agree'], ordered = True)

print(census['higher_tax'].unique())

# Use cat.codes to label encode the higher_tax variable
census['higher_tax'] = census['higher_tax'].cat.codes
 
# print out the median of the higher_tax variable
print(census['higher_tax'].median()) 

# Use get_dummies to OHE the marital_status
census = pd.get_dummies(census, columns=['marital_status'])
 
# print out the first 5 rows in the census dataframe
print(census.head())