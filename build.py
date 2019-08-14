'''
import speech_recognition as sr
import win32com.client as wincl
import tkinter as tk
from tkinter import messagebox, simpledialog
from geopy.geocoders import Nominatim
from pyautogui import press, typewrite, hotkey
import time,arduinocomm,threading
import wolframalpha,re,string,datetime,random,urllib3,os, serial, base64
'''
import os
from base64 import *
if 'setup.config' not in os.listdir(os.getcwd()):
    import setup
else:
    import human_interface
