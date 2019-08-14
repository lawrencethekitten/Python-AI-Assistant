import speech_recognition as sr
import win32com.client as wincl
from pyautogui import press, typewrite, hotkey
import understanding,time,arduinocomm,threading
eraseFirstRun=False
with open('setup.config') as search:
    for line in search:
        line = line.rstrip()  # remove '\n' at end of line
        if "transcribe " in line:
            transcribe=line.replace('transcribe ','')
def say(text):
    speak = wincl.Dispatch("SAPI.SpVoice")
    print(text)
    speak.Speak(text)
import understanding,time,arduinocomm,threading
def listen():
    try:
        with mic as source:
            print("listening")
            #arduinocomm.write('l')
            audio = r.listen(source)
            #recognizer.adjust_for_ambient_noise(source)
        print("transcribing...")
        arduinocomm.write('t')
        dialog=r.recognize_google(audio).lower()
        if transcribe=='True':
            with open('transcribedText.log',mode='a') as file:
                file.write(dialog)
                file.write('\n')
        else:
            pass
        say(understanding.processor(dialog))
        #return dialog
    except sr.UnknownValueError:
        say("")
def listenDebug():
    with mic as source:
        print("listening")
        audio = r.listen(source)
        #recognizer.adjust_for_ambient_noise(source)
    print("transcribing...")
    dialog=r.recognize_google(audio).lower()
    #if dialog=='update':
    #    import processor
    with open('transcribedText.log',mode='a') as file:
        file.write(dialog)
        file.write('\n')
    say(understanding.processor(dialog))
with open('setup.config') as search:
    for line in search:
        line = line.rstrip()  # remove '\n' at end of line
        if "name " in line:
            name=line.replace('name ','')
        elif 'firstrun' in line:
            eraseFirstRun=True
            say('Welcome to the python assistant (name pending). Here is a demo to show you just what I can do.')
            import demo
if eraseFirstRun==True:
    with open("setup.config", "r") as f:
        lines = f.readlines()
    with open("setup.config", "w") as f:
        for line in lines:
            if line.strip("\n") != "firstrun":
                f.write(line)

say("Hello {}".format(name))
r = sr.Recognizer()
mic = sr.Microphone()
while True:
    listen()
