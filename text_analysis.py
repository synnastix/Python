import os
import zipfile
import re
import xml.dom.minidom
import nltk
import string
import collections
import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

# Set variables
document = 'document.docx' # Specify document to be analyzed
workbook = 'results.xlsx' # Specificy results file
combo = 1  # Minimum word combinations
max_combo = 4  # Maximum word combinations
max_res = 100 # Maximum results per pass

# Clean up doc file
docx = zipfile.ZipFile(document)
content = docx.read('word/document.xml').decode('utf-8')
cleaned = re.sub('<(.|\n)*?>','',content)

# Lowercase
text = cleaned
lower_text = text.lower()

# Tokenize words
tokenized_word = word_tokenize(lower_text)
tokenized_word = [word for word in tokenized_word if word.isalpha()]

# Remove stop words
stop_words = set(stopwords.words("english")) # Change language to process other languages
cleaned = [word for word in tokenized_word if word not in stop_words]

# Initialize workbook
writer = pd.ExcelWriter(workbook)

# Scrape data and add to book
while (combo <= max_combo):
    # Identify ngrams
    esBigrams = ngrams(cleaned, combo)
    esBigramFreq = collections.Counter(esBigrams)

    # Get results
    results = esBigramFreq.most_common(max_res)

    # Create dataframe
    df = pd.DataFrame(data=results)

    # Write to workbook
    sheetname = str(combo) + ' Word'
    df.to_excel(writer, sheetname, index=False)
    writer.save()

    # Iterate
    combo = combo + 1
