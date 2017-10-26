import zipfile
import optparse

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		return password
	except:
		return 

def main():
	parser = optparse.OptionParser("Please add the following arguments for processing: "+\
	"-f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest='zname', type='string',\
	help='specify zip file')
	parser.add_option('-d', dest='dname', type='string',\
	help='specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname
	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)
	for line in passFile.readlines():
		password = line.strip('\n')
		guess = extractFile(zFile, password)

		#If the password is found
		if guess:
			print '[+] Found it ' + password + '\n'
			exit(0)

	#If password not found in dictionary
	print '[-] Password not in specified dictionary'
			
if __name__ == '__main__':
	main()
