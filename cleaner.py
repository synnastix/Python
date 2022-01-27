import pandas as pd

# Specify inputs / outputs

data = 'test.csv' # This is your source data
wordlist = 'wordlist.csv' # This is your list of terms for searching
true_out = 'junk.csv' # Rows where a match was found will end up here
false_out = 'not_junk.csv' # Rows where a match was not found will end up here
colx = 'col2' # Specify column to search within based on your column headers in your data
colz = 'key' # Specify column to load based on your column header in your wordlist

# Read in csv as dataframe and normalize data to check in lower case
df = pd.read_csv(data)
df[colx] = df[colx].str.lower()

# Read in csv as wordlist and normalize in lower case
list_csv = pd.read_csv(wordlist)
list = list_csv[colz].tolist()  # Convert column to list

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
