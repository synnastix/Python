import pandas as pd
import openpyxl

# Specify inputs / outputs

data = 'data.xlsx' # This is your source data
wordlist = 'wordlist.txt' # This is your list of terms for searching
true_out = 'true_rows.csv' # Rows where a match was found will end up here
false_out = 'false_rows.csv' # Rows where a match was not found will end up here
colx = 'text' # Specify column to search within based on your column headers in your data
colz = 'key' # Specify column to load based on your column header in your wordlist if using CSV

# Read in data as dataframe and normalize data to check in lower case
# df = pd.read_csv(data)
df = pd.read_excel(data, engine='openpyxl')

df[colx] = df[colx].str.lower()

# Read in csv as wordlist
#list_csv = pd.read_csv(wordlist)
#list = list_csv[colz].tolist()  # Convert column to list

# Read text file as wordlist
list = [line.strip() for line in open(wordlist,'r')]

# Normalize list in lowercase
for i in range(len(list)):
    list[i] = list[i].lower()

# Check and append true / false test
df['test'] = df[colx].apply(lambda x: any([k in x for k in list]))

# Split data based on true / false test and output to file

isjunk = df[df.test]
isjunk.to_csv(true_out)

notjunk = df[~df.test]
notjunk.to_csv(false_out)

# Let me know something happened
print('All clean.')
