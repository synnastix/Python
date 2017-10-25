# Violent Python 

import crypt
import hashlib

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		if (cryptWord == cryptPass or hashlib.sha512(word) == cryptPass):
			print "[+] Here it is: "+word+"\n"
			return
	print "[-] No dice. \n"
	return

def main():
	passFile = open('passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Checking Password For: "+user
			testPass(cryptPass)

if __name__ == "__main__":
	main()
