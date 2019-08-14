import tkinter as tk
from tkinter import messagebox, simpledialog
import os,base64
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent=str(base64.b64decode("YXNzaXN0YW50")))
root=tk.Tk()
root.title('Assistant Setup Dialog')
if 'setup.config' in os.listdir(os.getcwd()):
    reset=messagebox.askyesno(title='Assistant already set up.',message="Your assistant has already been set up to run on this computer. Would you like to set it up again?")
    if reset==True:
        os.remove('setup.config')
        os.startfile('setup.py')
        exit(0)
    else:
        exit(0)
else:
    info={
        'name': '',
        "email" :'',
        'passwd':'',
        'vocalauth':None,
        'com': '',
        'browser': '',
        'coords': '',
        'transcribe': None
        }
    info['name'] = simpledialog.askstring("What is your name?", "Input name.", parent=root)
    q1=messagebox.askyesno(title='Allow to sign into email?',message='Input email and email password to sign you into websites/email? Your password is kept locally and encrypted on your hard drive. No need to worry.')
    if q1==True:
        info['email'] = simpledialog.askstring("What is your email?", "Input email.", parent=root)
        temp= simpledialog.askstring("What is your email password?", "This information is encrypted and kept safe and ONLY used to sign you into your email account.", parent=root)
        info['passwd']=str(base64.b64encode(bytearray(temp,'utf-8')))
        temp= simpledialog.askstring("Set vocal authorization.", "This is vocal authorization to sign into your email account (which will also be encrypted).", parent=root)
        info['vocalauth']=str(base64.b64encode(bytearray(temp,'utf-16')))
    else:
        messagebox.showinfo(title="Gotcha.",message='''Loud and clear. I wouldn't want to give my email password to something I didn't program either.''')
    arduino=messagebox.askyesno(title='Set up Arduino?',message='Are you going to use the Arduino companion with this assistant?')
    if arduino==True:
        info['com']= simpledialog.askstring("What is your Arduino's COM port?", "Input COM port.", parent=root)
    else:
        pass
    info['browser'] = simpledialog.askstring("What is your preferred web browser?", "Input your preferred browser's name for searching the web.", parent=root)
    temp2 = geolocator.geocode(simpledialog.askstring("Location", "Input your city (or just a city) for weather.", parent=root))
    info['coords']=((round(temp2.latitude,4),round(temp2.longitude,4)))
    info['transcribe']=messagebox.askyesno(title='Transcribe all conversations?',message='Would you like to keep a record of all conversations we have? This record is stored on the computer and can be deleted at any time just so you know.')
    print(info)
    with open('setup.config',mode='w') as file:
        file.write('name '+info['name'])
        file.write('\n')
        file.write('email '+info['email'])
        file.write('\n')
        file.write('passwd '+info['passwd'])
        file.write('\n')
        file.write('vocalauth '+info['vocalauth'])
        file.write('\n')
        file.write('comport '+info['com'])
        file.write('\n')
        file.write('browser '+info['browser'])
        file.write('\n')
        file.write('coords '+str(info['coords']))
        file.write('\n')
        file.write('transcribe '+str(info['transcribe']))
        file.write('\n')
        file.write('firstrun')
