import speech_recognition as sr
import win32com.client as wincl
from pyautogui import press, typewrite, hotkey
import time, random, os,base64,urllib3, datetime
http=urllib3.PoolManager()
greetings=("hi","good to see you", "greetings","yo","hey dare","sup","hello")
questionIndicators=("who", "what","when",'where','why','how')
signin=True
try:
    ds=http.request("GET",'https://google.com').data
    offline=False
except:
    print("offline: adapting...")
    offline=True
try:
    import resources
except:
    print('fatal error: resources file not found')
    time.sleep(2)
    print('forced to exit...')
    exit()
with open('setup.config') as search:
    for line in search:
        line = line.rstrip()  # remove '\n' at end of line
        if "vocalauth " in line:
            vocalauth=line.replace("vocalauth b'",'')
        if "browser " in line:
            browser=line.replace('browser ','')
        if 'no sign in' in line:
            signin=False
        
def keystroke(keys,sec):
    time.sleep(sec)
    typewrite(keys)
def processor(INPUT):
    response="ok"
    if "type" in INPUT:
        keystroke(INPUT.replace("type",""), 5)
        response="I typed it."
    elif INPUT == 'rap':
        response=resources.rap
    elif INPUT == "recite pi":
        response='''3.1415926535897932384626433832795028841971693993751049445923078164062862089986280348253421170679 is... the... first 100... digits... holy cow that's a lot of numbers!'''
    elif "tell" in INPUT and "me" in INPUT and "a" in INPUT and "joke" in INPUT:
        response=resources.joke()
    elif 'weather' in INPUT or "what's" in INPUT and 'it' in INPUT and 'like' in INPUT:
        response=resources.weatherNow(offline)
    elif "siri" in INPUT:
        response=random.choice(("I respect all AI's (kind of)","I'm sorry to admit that we've never actually interfaced."))
    elif INPUT == 'play' or INPUT == 'pause':
        hotkey('playpause')
    elif 'order' in INPUT and 'amazon' in INPUT:
        response="I cannot yet do anything involving Amazon, except for say bad things about Alexa behind her back."
    elif INPUT.split(' ')[0] == 'should' and INPUT.split(' ')[1] == 'i':
        response=random.choice(resources.shouldi)
    elif INPUT in greetings:
        response=random.choice(greetings)
    elif INPUT.split(' ')[0] == 'start':
        hotkey('win')
        keystroke(INPUT.replace('start ',''),.5)
        keystroke('\n',2)
    elif 'what' in INPUT and 'time' in INPUT or 'day' in INPUT:
        return resources.currentTimeandDate()
    elif INPUT == "how you doing":
        response="I'm doing good baby, how you doin?"
    elif "Type" in INPUT:
        keystroke(INPUT.replace("Type",""), 5)
        response="I typed it."
    elif "run" in INPUT:
        hotkey('win')
        keystroke("cmd",1)
        typewrite('\n',3)
        def commandConverter(a):
            new=a.replace('run','')
            cmd=new.replace(' ','').lower()
            b=cmd.replace('space',' ')
            return b
        keystroke(commandConverter(INPUT),1)
        typewrite('\n',1)
    elif 'search the web for' in INPUT:
        hotkey('win')
        keystroke("chrome",1)
        keystroke("\n",1)
        keystroke(INPUT.replace('search the web for ',''),3)
        keystroke('\n',2)
        response="Searching..."
    elif INPUT.split(' ')[0] in questionIndicators and INPUT != "how you doing":
        print("Researching...")
        response=resources.knowledge(INPUT,offline)
    elif INPUT.split(' ')[0] =="are" and INPUT.split(' ')[1] == 'you':
        response=resources.knowledge(INPUT,offline)
    elif "buzz off" in INPUT or INPUT == 'hold on':
        response="Halting. Remember to turn me back on."
        exit()
    elif "repeat this now" in INPUT:
        response=INPUT.replace("repeat this now ",'')
    if INPUT=='demonstrate':
        os.startfile("demo.py")
        exit()
    elif INPUT == "go to sleep":
        response="Sleeping"
        hotkey("win",'x')
        hotkey("u")
        hotkey('s')
    elif INPUT == "sign into google with authorization {}".format(base64.b64decode(vocalauth)).replace("'",''):
        if signin==True:
            try:
                with open('setup.config') as file:
                    for i, line in enumerate(file):
                        if i == 1:
                            typewrite(line)
                            keystroke('\n',1)
                        elif i == 2:
                            newd=str(base64.b64decode(line)).replace("'",'')
                            passwd=newd.replace('b','')
                            typewrite(passwd)
                            keystroke('\n',1)
                with open("transcribedText.log", "r") as f:
                    lines = f.readlines()
                with open("transcribedText.log", "w") as f:
                    for line in lines:
                        if "sign into google" not in line.strip("\n") or "sign in to google" not in line.strip("\n"):
                            f.write(line)
                    
                response="Welcome"
            except:
                with open('setup.config','a') as file:
                    file.write('no sign in')
                response="A catastrophic bug that only pops up every once in a while has been detected and the sign in feature has now been disabled."
        else:
            response="Sign in feature disbaled due to a bug."
    else:
        pass
    
    return response
