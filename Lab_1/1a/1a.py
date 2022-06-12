import os
import getpass
user = getpass.getuser()
filenames = []

for root, dirs, files in os.walk("."):  
    for filename in files:
        filenames.append(filename)
        
print("1 - for block, 0 - unblock")
n = int(input())

if user == 'kali' or user == 'root':

	os.system("sudo chattr -i ext.tbl")
	os.system("sudo chmod 777 ext.tbl")
	
	with open('ext.tbl', 'r') as f:
		names = f.read().splitlines()
		for fnames in names:
			if fnames in filenames:
				if (n == 1):
			
					os.system("sudo chmod 000 {}".format(fnames))
					os.system("sudo chattr +i {}".format(fnames))
					print("{} is blocked".format(fnames))
				if (n == 0):
					os.system("sudo chattr -i {}".format(fnames))
					os.system("sudo chmod 777 {}".format(fnames))
					print("{} is unblocked".format(fnames))
			else:
				pass
				
else:
	print("acces denied")
