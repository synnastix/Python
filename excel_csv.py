#Script to take data from a mix of CSV and Excel files and merge into one single CSV file in a standard format.

import glob
import pandas as pd
import pyexcel
import os

#Define file paths for the source material and outputs
path = '/home/user/Desktop/practice/'
parsed = '/home/user/Desktop/practice/parsed/'
completed = '/home/user/Desktop/practice/completed/'

#Remove any old files so as to not contaminate the new data
old_completed = glob.glob(completed + '*')
old_parsed = glob.glob(parsed + '*')

for old in old_completed:
    os.remove(old)

for old in old_parsed:
    os.remove(old)

print "Done deleting old data"

#Convert any CSV files to Excel
def csv_convert():
    raw_csv = glob.glob(path + '*.csv')
    for raw in raw_csv:
        print 'Found' + raw + ', converting to Excel'
        sheet = pyexcel.get_sheet(file_name=raw)
        sheet.save_as(raw + '.xlsx')
    print "Done converting CSV files to Excel"

#Convert excel to csv and only grab specific columns
def excel_convert():    
    excel_files = glob.glob(path + '*xlsx') 
    for excel in excel_files:
        print 'Found' + excel + ', converting to csv'
        out = parsed + os.path.basename(excel.split('.')[0]+'.csv')
        df = pd.read_excel(excel) # if only the first sheet is needed.
        #Specify which columns to select by column header
        df2 = df.loc[:, ['Header 1', 'Header 2', 'Etc']]
        df2.to_csv(out) 
    print "Done grabbing needed data"

#Merge into single CSV file
def csv_merge():
    #grab all the parsed CSV files
    csv_files = glob.glob(parsed + '*.csv')
    #merge data into one file
    merged_csv = pd.concat([pd.read_csv(f) for f in csv_files])
    #export to a single csv
    merged_csv.to_csv(completed + 'merged_csv.csv')

csv_convert()
excel_convert()
csv_merge()

#success
print 'All Finished!'
