import pandas as pd

searchQuery = 'query'

df = pd.read_csv('input.csv')

#concatente multiple csv files into a single dataframe
#df = pd.concat(map(pd.read_csv, ['input.csv', 'input2.csv']))

dfFiltered = df.loc[df['filterColumn'].str.contains(searchQuery) == True]

print(dfFiltered)

print(searchQuery,'=',dfFiltered['sumColumn'].sum())

dfFiltered.to_csv (r'searchQuery.csv', index = False, header=True)
