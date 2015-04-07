#!/usr/bin/python
# -*- coding: utf-8 -*-

import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt','r')
	ctype = cryptPass.split("$")[1]

	if ctype == '6':
		salt = cryptPass.split("$")[2]
		insalt = "$" + ctype + "$" + salt + "$"
		for word in dictFile.readlines():
			word = word.strip('\n')
			cryptWord = crypt.crypt(word,insalt)
			if (cryptWord == cryptPass):
				print "[+] Found Password: "+word+"\n"
				return
		print "[-] Password Not Found.\n"
		return

def main():
	#passFile = open('/tmp/passwords.txt')
	passFile = open('sample-passwords.txt')
	for line in passFile.readlines():
		line = line.replace("\n","").split(":")
		if not line[1] in ['x','*','!']:
			user = line[0]
			cryptPass = line[1]
			print "[#] Cracking Password For: "+user
			testPass(cryptPass)

if __name__ == "__main__":
	main()
