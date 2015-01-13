import string
import os
from os import listdir
from os.path import isfile, join

def canAccess(stringPath, subBlacklist, blacklist):
	if (not os.path.exists(stringPath)):
		print("Directory does not exist.")
		return False
	for x in range (len(subBlacklist)):
		if (subBlacklist[x] in stringPath):
			print("Directory blacklisted")
			return False
	if(stringPath+"\n" in blacklist):
		print("Directory blacklisted")
		return False
	return True

def rename(stringPath, dirFiles):
	fileType = []
	for x in range (len (dirFiles)):
		print("Current name = %s" % dirFiles[x])
		newName = raw_input("Please enter the new name (press return to keep current name): ")
		if (newName != ''):
			if (not '.' in newName):
				fileType = string.rsplit(dirFiles[x],'.')
				os.rename((stringPath +'\\'+ dirFiles[x]), (stringPath +'\\'+ newName+'.'+fileType[len(fileType)-1]))
			else:
				os.rename((stringPath +'\\'+ dirFiles[x]), (stringPath +'\\'+ newName))
			print("Success!\n")

def addBlacklist(firstRun):
	print("Type a directory to add it to the blacklist.")
	print("Enter '/#' (comment) to stop.")
	dirBlack = ''
	while (dirBlack != '/#'):
		dirBlack = raw_input("Add: ")
		if (dirBlack != '/#'):
			firstRun.write(dirBlack+'\n')

def firstRun():
	print("Generating blacklist file...")
	firstRun = open("blacklist.txt",'w')
	firstRun.write("/#This is the blacklist file for MassRename\n")
	firstRun.write("/#lines begining with '/#' are comments\n")
	firstRun.write("/# add '*' after a directory to blacklist all subdirectories\n")
	choice = raw_input("Would you like to blacklist directories now? Y/N: ")
	if (choice == 'Y' or choice == 'y'):
		addBlacklist(firstRun)
	firstRun.close()

def initialize():
	if (os.name == "nt"):
		os.system("cls")
	else:
		os.system("clear")

	if(not os.path.exists("blacklist.txt")):
		firstRun()
	blackFile = open("blacklist.txt","r")	

	blacklist = []
	subBlacklist = []

	for line in blackFile:
		if(not '/#' in line):
			if('*' in line):
				subBlacklist.append(line[:-2])
			else:
				blacklist.append(line)
	blackFile.close()
	return blacklist, subBlacklist

def main():
	valid = False

	blacklist, subBlacklist = initialize()
	print("Welcome to this mass renaming program!")
	print("Please enter the directory where you want to mass rename")

	while not valid:
		stringPath = raw_input("Dir : ")
		valid = canAccess(stringPath, subBlacklist, blacklist)
		
	dirFiles = [ f for f in listdir(stringPath) if isfile(join(stringPath,f)) ]

	rename(stringPath, dirFiles)
	print("\n\nAll done! :D")

main()
