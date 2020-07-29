# Multi-purpose data manipulation assuming an input csv with 'year', 'thing', 'value' columns

import pandas as pd

# Options to set for column width and rows

#pd.set_option('display.max_colwidth', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

# Read the data - encoding optional
df = pd.read_csv("data.csv", encoding='ISO-8859-1')

# Trim whitespace that may cause issues
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Groupby value
df1 = df.groupby(['year', 'thing']).sum()

# Create pivot table
df2 = df.groupby(['year','thing'],as_index = False).sum().pivot('year','thing').fillna(0)

# Cumulative sum
df3 = df['cumulativesum'] = df.groupby('thing')['value'].transform(lambda g: g.cumsum())
df3 = df.set_index('year')

# Output
print (df3)
