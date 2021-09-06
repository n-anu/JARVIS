import os
import cv2
import time
import pyttsx3
import random
import playsound
import pyautogui
import noisereduce as nr
import speech_recognition as sr
from gtts import gTTS
import psutil
import string
from datetime import datetime

def restart():
    os.system("gnome-terminal -e 'sudo reboot'")
    time.sleep(2)
    pyautogui.press(['k', 'enter'])

def shutdown():
    os.system("gnome-terminal -e 'sudo shutdown 0'")
    time.sleep(2)
    pyautogui.press(['k', 'enter'])

def google(text):
    os.system("gnome-terminal -e 'firefox --search text'")

def firefox(search):
    search = "'" + search + "'"
    text = "firefox --search " + search
    os.system(text)
    
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "audio.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speak1(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[24].id)
    engine.setProperty('rate',160)
    engine.say(text)
    engine.runAndWait()

def music():
    os.system("gnome-terminal -e 'firefox youtube.com'")
    time.sleep(5)
    speak("Tell me, music name please?")
    pyautogui.press('tab',presses=6)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press(['tab','enter'])

def movie():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,phrase_time_limit=5)
        text = r.recognize_google(audio)
        speak("You want to see:" + text)
        return text

def name():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,phrase_time_limit=3)
        text = r.recognize_google(audio)
        return text

def Camera():
    os.system("gnome-terminal -e 'cheese'")
    time.sleep(2)
    speak("If you want to take photo say PHOTO")
    s = 1
    while(s):
        battery()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("Please Say Something:")
            #r.adjust_for_ambient_noise(source)
            audio = r.listen(source,phrase_time_limit=5)
            #audio = nr.reduce_noise(audio)
            try:
                command = r.recognize_google(audio)
                if ("close camera" == command.lower()) or ("exit" == command) or ("quit" == command) or ("close" == command):
                    pyautogui.hotkey('ctrl','q')
                    s = 0
                elif ("take a photo" == command.lower()) or ("photo" == command.lower()):
                    pyautogui.press('space')
            except:
                continue

def screenshot1():
    im = pyautogui.screenshot()
    speak("do you want to see screenshot?")
    time.sleep(1)
    text = name()
    if text.lower() == "yes":
        while True:
            text = name()
            if text.lower()=="exit":
                pyautogui.press('q')
            cv2.imshow()
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break

     
def battery():
    var = 1
    while var:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        #print("%d",int(percent[2]) - int('0'))
        percent = round(float(percent),2)
        percent2 = str(percent)
        plugged = "Plugged In" if plugged else "Unplugged"
        if (percent < 30) and (plugged == "Unplugged"):
            speak("Battery is low. Only "+ percent2 +"percent battery remains. Please Plug In.")
        elif ((percent == 100.0 or percent == 100 or percent == 100.00) and plugged == "Plugged In"):
            speak("Battery is Fully charged. Please unplug your charger.")
        else:
            var = 0

def youtube():
    os.system("gnome-terminal -e 'firefox youtube.com'")
    time.sleep(5)
    speak("Tell me, What do you want to search?")
    pyautogui.press('tab',presses=6)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press(['tab','enter'])
    time.sleep(10)
    s = 1
    while(s):
        battery()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("Please Say Something:")
            #r.adjust_for_ambient_noise(source)
            audio = r.listen(source,phrase_time_limit=5)
            #audio = nr.reduce_noise(audio)
            try:
                command = r.recognize_google(audio)
                c = 0
                if ("close this tab" == command) or ("exit" == command) or ("quit" == command) or ("close" == command):
                    pyautogui.hotkey('ctrl','w')
                    s = 0
                elif "next song" == command:
                    pyautogui.press(['tab','tab','tab','enter'])
                    c = c+1
                elif ("previous song" == command) and (c > 0):
                    pyautogui.hotkey('alt','left')
                elif "forward" == command:
                    pyautogui.press('right',presses=4)
                elif "backward" == command:
                    pyautogui.press('left',presses=4)
                elif ("volume up" == command) or ("increase volume" == command):
                    pyautogui.press('up')
                elif ("volume down" == command) or ("decrease volume" == command):
                    pyautogui.press('down')
                elif ("pause" == command) or ("resume" == command) or ("start" == command) or ("stop" == command):
                    pyautogui.press('space')
                elif ("full screen" == command):
                    pyautogui.press('f')
            except:
                continue

def keyboard():
    speak("Hello Sir, You have now full access to keyboard.")
    key = 1
    while(key):
        battery()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("Please Say Something:")
            #r.adjust_for_ambient_noise(source)
            audio = r.listen(source,phrase_time_limit=2)
            #audio = nr.reduce_noise(audio)
            try:
                command = r.recognize_google(audio)
                if "tab" == command:
                    pyautogui.press('tab')
                elif "space" == command:
                    pyautogui.press('space')
                elif "enter" == command:
                    pyautogui.press('enter')
                elif "backspace" == command:
                    pyautogui.press('backspace')
                elif "left" == command:
                    pyautogui.press('left')
                elif ("up" == command) or ("up arrow" == command):
                    pyautogui.press('up')
                elif ("down" == command) or ("down arrow" == command):
                    pyautogui.press('down')
                elif "press tab" == command:
                    pyautogui.keyDown('tab')
                    speak("tab key pressed")
                elif "release tab" == command:
                    pyautogui.keyUp('tab')
                    speak("tab key released")
                elif "press control" == command:
                    pyautogui.keyDown('ctrl')
                    speak("control key pressed")
                elif "release control" == command:
                    pyautogui.keyUp('ctrl')
                    speak("control key released")
                elif "press alt" == command:
                    pyautogui.keyDown('alt')
                    speak("alt key pressed")
                elif "release alt" == command:
                    pyautogui.keyUp('alt')
                    speak("alt key released")
                elif "press function" == command:
                    pyautogui.keyDown('fn')
                    speak("function key pressed")
                elif "release function" == command:
                    pyautogui.keyUp('fn')
                    speak("function key released")
                elif "escape" == command:
                    pyautogui.press('esc')
                elif "screenshot" == command:
                    pyautogui.hotkey('windows','prntscrn')
                elif "press shift" == command:
                    pyautogui.keyDown('shift')
                    speak("shift key pressed")
                elif "release shift" == command:
                    pyautogui.keyUp('shift')
                    speak("shift key released")
                elif "press home key" == command:
                    pyautogui.keyDown('windows')
                    speak("home key pressed")
                elif "release home key" == command:
                    pyautogui.keyUp('windows')
                    speak("home key released")
                elif "numlock" == command:
                    pyautogui.press('numlock')
                elif "right arrow" == command:
                    pyautogui.press('right')
                elif "left arrow" == command:
                    pyautogui.press('left')
                elif "up arrow" == command:
                    pyautogui.press('up')
                elif "down arrow" == command:
                    pyautogui.press('down')
                elif "one" == command:
                    pyautogui.press('1')
                elif "two" == command:
                    pyautogui.press('2')
                elif "three" == command:
                    pyautogui.press('3')
                elif "four" == command:
                    pyautogui.press('4')
                elif "five" == command:
                    pyautogui.press('5')
                elif "six" == command:
                    pyautogui.press('6')
                elif "seven" == command:
                    pyautogui.press('7')
                elif "eight" == command:
                    pyautogui.press('8')
                elif "nine" == command:
                    pyautogui.press('9')
                elif "zero" == command:
                    pyautogui.press('0')
                elif ("exit" == command) or ("quit" == command) or ("out" == command):
                    speak("Hope you enjoyed by accessing keyboard.")
                    key = 0
                elif "a" == command:
                    pyautogui.press('a')
                elif "b" == command:
                    pyautogui.press('b')
                elif "c" == command:
                    pyautogui.press('c')
                elif "d" == command:
                    pyautogui.press('d')
                elif "e" == command:
                    pyautogui.press('e')
                elif "f" == command:
                    pyautogui.press('f')
                elif "g" == command:
                    pyautogui.press('g')
                elif "h" == command:
                    pyautogui.press('h')
                elif "i" == command:
                    pyautogui.press('i')
                elif "j" == command:
                    pyautogui.press('j')
                elif "k" == command:
                    pyautogui.press('k')
                elif "l" == command:
                    pyautogui.press('l')
                elif "m" == command:
                    pyautogui.press('m')
                elif "n" == command:
                    pyautogui.press('n')
                elif "o" == command:
                    pyautogui.press('o')
                elif "p" == command:
                    pyautogui.press('p')
                elif "q" == command:
                    pyautogui.press('q')
                elif "r" == command:
                    pyautogui.press('r')
                elif "s" == command:
                    pyautogui.press('s')
                elif "t" == command:
                    pyautogui.press('t')
                elif "u" == command:
                    pyautogui.press('u')
                elif "v" == command:
                    pyautogui.press('v')
                elif "w" == command:
                    pyautogui.press('w')
                elif "x" == command:
                    pyautogui.press('x')
                elif "y" == command:
                    pyautogui.press('y')
                elif "z" == command:
                    pyautogui.press('z')
            except:
                continue

def welcome():
    h = int(datetime.now().hour)
    if h>=4 and h < 12:
        speak("Good Morning Sir, I am JARVIS.")
    elif h>= 12 and h < 18:
        speak("Good Afternoon Sir, I am JARVIS.")
    elif h>=18 and  h<24:
        speak("Good Evening Sir, I am JARVIS.")
    else:
        speak("Good Night Sir, Its time to Sleep.")
        shutdown()

p = 1
welcome()

while(p):
    battery()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Please Say Something:")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source,phrase_time_limit=5)
        #audio = nr.reduce_noise(audio)
        text = "1"
        text1 = "1"

        try:
            text = r.recognize_google(audio)
            text2 = text
            print('You said:{}'.format(text))
            if "how are you" == text:
                speak("I am fine. How about you?")
            elif ("hello" == text.lower()) or ("hello jarvis" == text.lower()):
                array = ['Hello Sir','Yes Sir']
                text = random.choice(array)
                speak(text)
            elif "who are you" == text:
                speak("Hello Sir, I am JARVIS.")
            elif ("quit" == text) or ("exit" == text) or ("turn off yourself" == text) or ("Jarvis sleep" == text):
                array = ['Okay Sir, Have a nice day.','Bye Sir, I hope you enjoyed.','Bye Sir, Have a nice day.']
                text = random.choice(array)
                speak(text)
                p = 0
            elif ("call" == text) or ("make a call" == text) or ("Jarvis make a call" == text):
                speak("Whom do you want to call Sir? Or say No for another command.")
                text2 = name()
                if text2=="no":
                    speak("Okay Sir.")
                else :
                    speak("You want to call " + text2 + "Just wait a second Sir. I am calling " + text2)
            elif "what can you do" == text:
                speak("I can do anything for what I was made.")
            elif "screenshot" == text.lower():
                screenshot1()
            elif "keyboard" == text:
                keyboard()
            elif ("say clearly" == text) or ("repeat" == text):
                speak(text2)
                text1 = text
            elif ("open new terminal" == text) or ("new terminal" == text):
                pyautogui.hotkey('windows','t')
            elif ("open camera" == text.lower()) or ("take a photo" == text.lower()):
                speak("opening Camera")
                Camera()
            elif ("music" == text) or ("play music" == text):
                music()
            elif ("movie" == text) or ("play movie" == text):
                speak("At this moment only those movies are available which are on YouTube.")
                youtube()
                #speak("which movie you want to see Sir?")
                #text2 = movie()
            elif ("restart" == text) or ("restart Jarvis" == text) or ("restart system" == text) or ("restart system Jarvis" == text) or ("Jarvis restart system" == text) or ("Jarvis restart" == text) or ("reboot" == text) or ("reboot Jarvis" == text) or ("reboot system" == text) or ("reboot system Jarvis" == text) or ("Jarvis reboot system" == text) or ("Jarvis reboot" == text):
                speak("your system is going to restart.")
                restart()
            elif ("shutdown" == text) or ("shutdown Jarvis" == text) or ("shutdown system" == text) or ("shutdown system Jarvis" == text) or ("Jarvis shutdown system" == text) or ("Jarvis shutdown" == text):
                speak("your system is going to shutdown.")
                shutdown()
            elif ("open Google" == text) or ("Jarvis open Google" == text) or ("Google search" == text) or ("do a Google search" == text) or ("Jarvis do a Google search" == text):
                speak("What do you want to search Sir?")
                search = name()
                firefox(search)
            elif ("open YouTube" == text) or ("Jarvis open YouTube" == text):
                speak("opening youtube")
                youtube()
            elif ("send sms" == text):
                speak("Whom do you want to send sms Sir? Tell me name? Otherwise say No.")
                text2 = name()
                if text=="no":
                    speak("Okay Sir.")
                else :
                    speak("You want to send sms to" + text2 + "Just wait a second Sir. I am sending sms.")
        except:
            if text != "1":
                print('you said ' + text)
            #    speak("you just said " + text) 
            #    speak("It is not in my commands. If you mean something else. Please say again.")
            #else:
            #    speak("I am sorry. I didn't hear anything from you. Please say again.")   
        text1 = text
        text = "1"







