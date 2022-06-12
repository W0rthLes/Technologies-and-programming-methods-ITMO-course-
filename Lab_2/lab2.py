from tkinter import *
import tkinter
import os
from tkinter import messagebox
from textwrap import wrap
import configparser
from cryptography.fernet import Fernet
import re

path = os.getenv('APPDATA')+'\TimpProg'
path1 = os.getcwd()+'\data_names.txt'
num = None
def encrypt(filename):

  f = Fernet(b'SJSTW3J7pGmZOI16CfcrVX1n24md0guwrXJC66eTFaI=')
  with open (filename, 'rb') as file:
    file_data = file.read()
  encrypted_data = f.encrypt(file_data)
  with open(filename, 'wb') as file:
    file.write(encrypted_data)
  
    
def decrypt(filename):
  f = Fernet(b'SJSTW3J7pGmZOI16CfcrVX1n24md0guwrXJC66eTFaI=')
  with open (filename, 'rb') as file:
    encrypted_data = file.read()  
    decrypted_data = f.decrypt(encrypted_data)
  with open(filename, 'wb') as file:
    file.write(decrypted_data)


def checkLicense():
  #################################################
  config = configparser.ConfigParser()
  config.read(path+'\config.ini')
  license_status = config['DEFAULT']['license']
  ##################################################
  if license_status == '0':
    
    license_label.configure(text='Статус лицензии - неактивна')
    license_label.grid(column=0, row=10)

    return False

  if license_status == '1':

    license_label.configure(text='Статус лицензии - активна')
    line_for_time['text'] = 'Время не ограничено!'
    license_label.grid(column=0, row=10)
    #btn_for_license = Button(window, text='Отправить', bg='Green', command=licenseButtonCheck)
    btn_for_license['state'] = 'disabled'
    btn_for_license.grid(column=0, row=21)    
    enter_license = Entry(window, width=40, state='disabled')
    enter_license.grid(column=0, row=20)  
    return True
    
ranPick = os.listdir(os.getenv('APPDATA'))
ranDir = '\\'+ranPick[-2]+'\\casual_data.dll'  

def init():

  if not os.path.isdir(path):    
    os.mkdir(path)
    #win32api.SetFileAttributes(path,win32con.FILE_ATTRIBUTE_HIDDEN)
         
  if os.path.exists(path+'\config.ini') and os.path.exists(os.getcwd()+'\data_names.txt'):
    
    with open(os.getenv('APPDATA')+ranDir, 'a+') as f:
      #win32api.SetFileAttributes(os.getenv('APPDATA')+ranDir,win32con.FILE_ATTRIBUTE_HIDDEN)
      pass
    
    with open(os.getenv('APPDATA')+ranDir, 'r') as f:
      with open(path+'\config.ini', 'r') as file:
        true_info = file.read()
        extra_info = f.read()
    if true_info == extra_info:
      print('ok')
    else:
      with open(path+'\config.ini', 'w') as file:
        file.write(extra_info)
    
    
    
  else:    
    config = configparser.ConfigParser()
    config.read(path+'\config.ini')
    config['DEFAULT']['timeleft'] = '60'
    config['DEFAULT']['license'] = '0'
        
    with open(path+'\config.ini', 'w') as f:     
      config.write(f)
    encrypt(path+'\config.ini')    
    #win32api.SetFileAttributes(path+'\config.ini',win32con.FILE_ATTRIBUTE_HIDDEN)
    
    if os.path.exists(os.getenv('APPDATA')+ranDir):
      with open(os.getenv('APPDATA')+ranDir, 'r') as f:
        with open(path+'\config.ini', 'r') as file:
          true_info = file.read()
          extra_info = f.read()
      if true_info == extra_info:
        print('ok')
      else:
        with open(path+'\config.ini', 'w') as file:
          file.write(extra_info) 
        
           
    with open(os.getcwd()+'\data_names.txt', 'w') as f: 
      pass
    
    
init() 
   
def onClick():
  userName = enter_text.get()
  if re.fullmatch(r'[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?', userName):
    names = list()
    
    with open(os.getcwd()+'\data_names.txt', 'r') as f:
        for line in f.readlines():
            names.extend(line.rstrip().split('\n'))
            
    with open(os.getcwd()+'\data_names.txt', 'a') as f:        
        if userName not in names:
            print(userName, file=f)
            userOut = 'Имя {} было добавлено'.format(userName)
            succesInfo.configure(text=userOut)
        else:
            userOut = 'Имя {} уже присутствует'.format(userName)
            succesInfo.configure(text=userOut)

    
  else:
    messagebox.showwarning('Уведомление', 'Нарушен формат ввода, попробуйте еще раз')

def on_closing():
  global num
  if messagebox.askokcancel('Выйти', 'Вы действительно хотите выйти?'):
    config = configparser.ConfigParser()
    config.read(path+'\config.ini')
    
    if num == None:
      encrypt(path+'\config.ini')
      with open(os.getenv('APPDATA')+ranDir, 'w+') as f:
        with open(path+'\config.ini', 'r') as file:
          info = file.read()
          f.write(info)
          
      window.destroy()
    else: 
      config['DEFAULT']['timeleft'] = str(num-1)
      with open(path+'\config.ini', 'w') as f:
          config.write(f)
      encrypt(path+'\config.ini')
      with open(os.getenv('APPDATA')+ranDir, 'w+') as f:
        with open(path+'\config.ini', 'r') as file:
          info = file.read()
          f.write(info)
      window.destroy()
      

def counter(count):
  global num
  if checkLicense():
    line_for_time['text'] = 'Время не ограничено!'
  else:
    line_for_time['text'] = 'Осталось времени: {} секунд'.format(count)
    
  if count > 0:
    if checkLicense():
      pass
    else:
      num = count
      window.after(1000, counter, count-1)
  else:
    if checkLicense():
      pass
    else:
      messagebox.showerror('Уведомление', 'Время вышло! Купите лицензию или удалите программу!')
      enter_text = Entry(window, width=50, state='disabled')
      enter_text.grid(column=0, row=1)
      btn = Button(window, text='Отправить', bg='LightGreen')
      btn['state'] = 'disabled'
      btn.grid(column=0, row=2)      

def licenseButtonCheck():
  global enter_license
  userLicense = enter_license.get()
  true_license = '1234567890'
  if userLicense == true_license:  
    config = configparser.ConfigParser()
    config.read(path+'\config.ini')
    config['DEFAULT']['license'] = '1'       
    with open(path+'\config.ini', 'w') as f:
        config.write(f)
    checkLicense()
    enter_text = Entry(window, width=50, state='normal')
    enter_text.grid(column=0, row=1)
    btn = Button(window, text='Отправить', bg='LightGreen')
    btn['state'] = 'normal'
    btn.grid(column=0, row=2)      
    enter_license = Entry(window, width=40, state='disabled')
    enter_license.grid(column=0, row=20)


    
window = Tk()
window.geometry('500x300+200+200')
window.resizable(width=False, height=False)
window.title("База имён")
txt = 'Введите необходимое ФИО в формате: "Фамилия Имя Отчество" на русском языке. В случае, если введенное Вами ФИО уже присутствует в базе, заново добавлено оно не будет.'
lbl = Label(window, anchor=tkinter.W,
            text=txt,
            font=('Arial Bold', 12))
lbl.grid(column=0, row=0)
window.update()


if lbl.winfo_width() > window.winfo_width():
    average_char_width = lbl.winfo_width() / len(txt)
    chars_per_line = int(window.winfo_width() / average_char_width)
    while lbl.winfo_width() > window.winfo_width():  
        wrapped_text = '\n'.join(wrap(txt, chars_per_line))
        lbl['text'] = wrapped_text
        window.update()
        chars_per_line -= 1
        
       
succesInfo = Label(window, anchor=tkinter.W, text='', font=('Arial Bold', 12))
succesInfo.grid(column=0, row=3)
  
enter_text = Entry(window, width=50)
enter_text.grid(column=0, row=1)
enter_text.focus()

btn = Button(window, text='Отправить', bg='LightGreen', command=onClick)
btn.grid(column=0, row=2)      

line_for_time = Label(window, text='', font=('Arial Bold', 12))
line_for_time.grid(column=0, row=4)

enter_license = Entry(window, width = 40)
enter_license.grid(column=0, row=20)

btn_for_license = Button(window, text='Отправить', bg='LightGreen', command=licenseButtonCheck)
btn_for_license.grid(column=0, row=21)      

license_label = Label(window, text='', font=('Arial Bold', 12))

window.protocol("WM_DELETE_WINDOW", on_closing)

decrypt(path+'\config.ini')
config = configparser.ConfigParser()
config.read(path+'\config.ini')
count = int(config['DEFAULT']['timeleft'])
counter(count)

window.mainloop()

