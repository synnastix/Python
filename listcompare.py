# Simple script to compare lists and identify overlap in an easily readable format

import optparse
import sys

#Defining the lists
list1 = []
list2 = []
list3 = []

def main():

	#Specify the files to compare
	parser = optparse.OptionParser("Please add the following arguments for processing: "+\
	"-f <first list> -s <second list>")
	parser.add_option('-f', dest='fname', type='string',\
	help='specify zip file')
	parser.add_option('-s', dest='sname', type='string',\
	help='specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.fname == None) | (options.sname == None):
		print parser.usage
		exit(0)
	else:
		fname = options.fname
		sname = options.sname

	#Read the first list into memory
	passFile = open(fname)
	for line in passFile.readlines():
		list1.append(line)

	#Read the second list into memory
	passFile = open(sname)
	for line in passFile.readlines():
		list2.append(line)

	#Compare the two lists
	for i in list2:
		if i in list1:
			list3.append(i)

	#Print the results
	print "The first list contains " + str(len(list1)) + " entries."
	print "The second list contains " + str(len(list2)) + " entries."
	print "Found " + str(len(list3)) + " overlapping item(s) which are listed below"
	for i in list3:
		sys.stdout.write(i)
		sys.stdout.flush()

main()
