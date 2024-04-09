from cv2 import meanShift
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import cv2
import pywhatkit as kit
from requests import get
import sys
import pyjokes as pj
import pyautogui
import time
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.encoders as encoders
import instaloader
import PyPDF2 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis2Ui import Ui_jarvis2Ui
import operator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
from twilio.rest import Client



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def news():
    main_url = "https://newsapi.org/"
    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first" ,"second" ,"third" ,"forth" ,"fifth" ,"sixth" ,"seventh" ,"eighth" ,"ninth" ,"tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        #print(day[i], ":", head[i])
        speak(f"{day[i]} news is {head[i]}")

def pdf_reader():
    book = open('Hacking.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak("The total number of pages in the pdf file is " + str(pages))
    speak("Sir please enter the page number you want me to read")
    pg = int(input("Enter the page number: "))
    Page = pdfReader.getPage(pg)
    text = Page.extract_text()
    speak(text)

class Mainthread(QThread):
    def __init__(self):
        super(Mainthread, self).__init__()

    def run(self):
        #self.TaskExecution()
        speak("please say wake up to continue")
        while True:
            self.query = self.takeCommand()
            if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
                self.TaskExecution()

    def takeCommand(self):
    #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

        try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")

        except Exception as e:
                #print(e)
                print("Say that again please...")
                return "None"
        return query

    def TaskExecution(self):
        if __name__ == "__main__":
            wishme()
            while True:
            #if 1:
                self.query = self.takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in self.query:
                    speak("Opening Youtube")
                    speak("Sir,What should i search on Youtube?")
                    cm = self.takeCommand().lower()
                    webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")
                elif'close youtube' in self.query:
                    speak("Closing Youtube")
                    os.system("TASKKILL /F /IM chrome.exe")                         
                
                elif 'open google' in self.query:
                    speak("Opening Google")
                    speak("Sir,What should i search on google?")
                    cm = self.takeCommand().lower()
                    webbrowser.open(f"{cm}")

                elif 'open stackoverflow' in self.query:
                    speak("Opening Stackoverflow")
                    webbrowser.open("stackoverflow.com")
                
                elif 'play music' in self.query:
                    speak("playing music")
                    music_dir = 'D:\\Songs'
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    print(songs)
                    os.startfile(os.path.join(music_dir, rd))

                elif 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'what time it is' in self.query:                    
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"sir , its adventure time , just kidding with you sir the real time is {strTime}")

                elif 'open code' in self.query:
                    speak("Opening Visual Studio Code")                
                    codepath = "Your vs code path"
                    os.startfile(codepath)
                elif'close code' in self.query:
                    speak("Closing Visual Studio Code")
                    os.system("TASKKILL /F /IM code.exe")
                
                elif 'open chrome' in self.query:
                    speak("Opening Google Chrome")
                    chrome = "Your Chrome path"
                    os.startfile(chrome)
                elif'close chrome' in self.query:
                    speak("Closing Google Chrome")
                    os.system("TASKKILL /F /IM chrome.exe")

                elif 'open notepad' in self.query:
                    speak("Opening Notepad")
                    notepad = "Your Notepad path"
                    os.startfile(notepad)
                elif'close notepad' in self.query:
                    speak("Closing Notepad")
                    os.system("TASKKILL /F /IM notepad.exe")

                elif 'open parade' in self.query:
                    speak("Opening Parade")
                    webbrowser.open("parade.com")


                elif 'open camera' in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(58)
                        if k==13:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                elif'play song on youtube' in self.query:
                    kit.playonyt("Song")

                elif 'ip address' in self.query:
                    ip = get('https://api.ipify.org').text
                    speak("Your public ip address is {}".format(ip))
                
                elif 'open cmd' in self.query:
                    os.system("start cmd")
                elif'close cmd' in self.query:
                    os.system("TASKKILL /F /IM cmd.exe")

                elif 'open spotify' in self.query:
                    speak("Opening Spotify")
                    cm = self.takeCommand().lower()
                    spotifypath = ("Path of spotify")
                    os.startfile(spotifypath) 
                elif'close spotify' in self.query:
                    speak("Closing Spotify")
                    os.system("TASKKILL /F /IM Spotify.exe")

                elif'you can go for now jarvis' in self.query:
                    speak("Bye Sir, Have a good day")
                    sys.exit()

                elif 'set alarm' in self.query:
                    speak("Setting alarm")
                nn = int(datetime.datetime.now().hour)
                if nn==12:
                    music_dir = 'D:\\Songs'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif'tell me a joke' in self.query:
                    joke=pj.get_joke()
                    speak(joke)
                    #print(joke)

                elif 'shutdown' in self.query:
                    speak("Sir, I am shutting down the system")
                    os.system("shutdown /s /t 1")

                elif 'restart' in self.query:
                    speak("Sir, I am restarting the system")
                    os.system("shutdown /r /t 1")

                elif 'sleep' in self.query:
                    speak("Sir, I am going to sleep")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                elif'open experience' in self.query:
                    speak("Opening Experience")
                    GeforcePath = "Path"
                    os.startfile(GeforcePath)
                elif'close experience' in self.query:
                    speak("Closing Experience")
                    os.system("TASKKILL /F /IM NVIDIA GeForce Experience.exe")

                elif'i am horney' in self.query:
                    speak("i am horny too")
                    speak("So lets just watch porn together , opening porn site")
                    porn = "https://goodporn.to/"
                    webbrowser.open(porn)
                
                elif'open steam' in self.query:
                    speak("Opening Steam")
                    Steampath = "Path"
                    os.startfile(Steampath)
                    speak("Sir, What game you want to Play?")
                if 'game' in self.query:
                        game = self.takeCommand().lower()
                        speak("Sir, I am playing {}".format(game))
                        os.system("start steam://rungameid/{}".format(game))
                elif'close steam' in self.query:
                    speak("Closing Steam")
                    os.system("TASKKILL /F /IM Steam.exe")

                elif'open discord' in self.query:
                    speak("Opening Discord")
                    Discordpath = "Path"
                    os.startfile(Discordpath)
                elif'close discord' in self.query:
                    speak("Closing Discord")
                    os.system("TASKKILL /F /IM Discord.exe")

                elif'send message' in self.query:
                    kit.sendwhatmsg("+91", "Hello, How are you?",14,20)

                elif'switch the window' in self.query:
                    speak("Switching the window")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab") 
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif'tell me the news' in self.query:
                    speak("Please wait sir,fetching the latest news")
                    news()

                elif'open amazon' in self.query:
                    speak("Opening Amazon")
                    speak("Sir,What should i search on Amazon?")
                    cm = self.takeCommand().lower()
                    webbrowser.open("https://www.amazon.in/s?k={}".format(cm))
                elif'close amazon' in self.query:
                    speak("Closing Amazon")
                    os.system("TASKKILL /F /IM chrome.exe")

                elif'book movie'in self.query:
                    speak("Booking movie")
                    webbrowser.open(("bookmyshow.com")) 
                
                elif'movie site' in self.query:
                    speak("Opening movie site")
                    webbrowser.open("https://moviesverse.co/")

                elif'open flipkart' in self.query:
                    speak("Opening Flipkart")
                    speak("Sir,What should i search on Flipkart?")
                    cm = self.takeCommand().lower()
                    webbrowser.open("https://www.flipkart.com/search?q={}".format(cm))
                elif'close flipkart' in self.query:
                    speak("Closing Flipkart")
                    os.system("TASKKILL /F /IM chrome.exe")

                elif'open instagram' in self.query:
                    speak("Opening Instagram")
                    webbrowser.open("https://www.instagram.com/")
                elif'close instagram' in self.query:
                    speak("Closing Instagram")
                    os.system("TASKKILL /F /IM chrome.exe")

          
            #Finding my location using Jarvis

                elif'where i am' in self.query or 'where we are' in self.query:
                    speak("wait sir, Let me check")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        city = geo_data['city']
                        country = geo_data['country']
                        speak("Sir i am not sure ,but we are in {} city of {}".format(city,country))
                    except Exception as e:
                        print(e)
                        speak("Sorry sir, due to network issue i am not able to tell you where we are")
                        pass

            #Instagram profile download and more stuff

                elif'instagram profile' in self.query or 'profile on instagram' in self.query:
                    speak("Sir please enter the username correctly")
                    name = input("Enter the username: ")
                    webbrowser.open("https://www.instagram.com/{}".format(name))
                    speak("Opening {} profile on instagram".format(name))
                    time.sleep(5)
                    speak("Sir would you like to download the profile picture of this account?")
                    condition = self.takeCommand().lower()
                    if 'yes' in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name,profile_pic_only=True)
                        speak("Sir,Profile picture has been downloaded in your main folder")
                    else:
                        pass

            #Taking SS by Jarvis

                elif'take a screenshot' in self.query or 'take ss' in self.query:
                    speak("Sir, please tell me the name of the screenshot file")
                    name = self.takeCommand().lower()
                    speak("Please wait Sir, i am taking a screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(name+".png")
                    speak("Screenshot has been saved in your main folder")

                elif'read pdf' in self.query or 'read the pdf' in self.query:
                    pdf_reader()

            #Hiding Files

                elif'hide all files' in self.query or 'hide this folder' in self.query or 'visible for everyone' in self.query or 'visible the folder' in self.query:
                    speak("Sir please tell me you want to hide this folder or visible for everyone")
                    condition = self.takeCommand().lower()
                    if 'hide' in condition:
                        os.system("attrib +h /s /d")
                        speak("Sir, this folder has been hidden")

                    elif 'visible' in condition:
                        os.system("attrib -h /s /d")
                        speak("Sir, this folder has been visible for everyone")

                    elif'leave it'in condition or 'leave it for now' in condition:
                        speak("ok Sir, i will leave it for now")

            #Mathematical sums using Jarvis

                elif"do some calculation" in self.query or "can you calculate" in self.query:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("Say what you want to calculate , example: 3 plus 3 ")
                        print("Listening......")
                        r.adjust_for_ambient_noise(source)
                        audio=r.listen(source)
                    my_string=r.recognize_google(audio)
                    print(my_string)
                    def get_operator_fn(op):
                        return {
                            "+" :operator.add,#plus
                            "-" :operator.sub,#minus
                            "x" :operator.mul,#multiplied by
                            'divided':operator.__truediv__,#divided
                            }[op]
                    def eval_binary_expr(op1,oper,op2):#5plus8
                        op1,op2=int(op1), int(op2)
                        return get_operator_fn(oper)(op1,op2)
                    speak("your result is")
                    speak(eval_binary_expr(*(my_string.split())))
                
                elif "temperature" in self.query:
                    search = ""
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "activate how to do mode" in self.query:
                    speak("How to mode is activated please tell me what you want to know")
                    how = self.takeCommand()
                    max_results = 1
                    how_to = search_wikihow(how,max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
                
                elif"how much power left"in self.query or"how much power we have"in self.query or"battery"in self.query:
                    battery=psutil.sensors_battery()
                    percentage=battery.percent
                    speak(f"sir our system have{percentage}percent battery")

                elif"internet speed" in self.query:
                    st=speedtest.Speedtest()
                    dl = st.download()
                    up = st.upload()
                    speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

                elif'volume up'in self.query:
                    pyautogui.press("volumeup")
                elif'volume down'in self.query:
                    pyautogui.press("volumedown")
                elif'volume mute'in self.query or'mute'in self.query:
                    pyautogui.press("volumemute")

                elif"hello" in self.query:
                    speak("hello sir, how can i help you")

                elif"how are you" in self.query:
                    speak("i am fine sir,what about you")

                elif"what are you doing" in self.query:
                    speak("waiting for your command")

                elif"tell me about yourself" in self.query:
                    speak("I am JARVIS sir , i am an AI who made by Rakshit Ojha")

                elif"who is rakshit" in self.query:
                    speak("he is my developer")

                elif"wallpapers" in self.query or "wallpaper" in self.query:
                    speak(" Opening wallpapers website")
                    speak("Sir,which type of wallpapers i search for you?")
                    cm = self.takeCommand().lower()
                    webbrowser.open(f"https://wall.alphacoders.com/{cm}")

   

                


                

                
                    

startExecution = Mainthread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvis2Ui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/OMEN/Downloads/ezgif.com-gif-maker (3).gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/OMEN/Downloads/jarvis-iron-man.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.ShowTime)
        timer.start(1000)
        startExecution.start()
    
    def ShowTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        
app = QApplication(sys.argv)
Jarvis = Main()
Jarvis.show()
exit(app.exec_())
                                   
