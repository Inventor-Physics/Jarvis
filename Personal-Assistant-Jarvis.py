from http import server 
import speech_recognition as sr
import requests
import json
import webbrowser
import pyautogui
import wikipedia
import time
import datetime
import pyttsx3
import smtplib 
import os

talk = True
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #if you want to turn the voice into a girl voice then simply change the number 0 to 1




def speak(audio):
    pass
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 
def news():
    nm= requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=1925d3c7e7174ea482e42db2080a2262')
    data = json.loads(nm.content)
    need = data['articles'][0]['description']
    print(need)
    speak(need)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('put your gmail account here', 'put your gmail password here') #in the place where it is written put your gmail here you may put your mail there and also put the password where it is written to
    server.sendmail('put your gmail here', to, content) #just put your gmail in the place where it is written do not remove double quotes and do not change anything else
    server.close()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, I am made by Inventor. Physics. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishme()
    while talk:
        query = takeCommand().lower() 

        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'hello' in query:
            speak("Hello sir, how may I help you ")
        elif 'open python website' in query:
            webbrowser.open("https://www.python.org/")
        elif 'about yourself' in query:
            speak("I am Jarvis, created by Inventor.Physics, And I am pleased to be with you , is there anything which I can help you with")
        elif 'story' in query:
            speak("Ok sir as you say. I found out an interesting story of war of worlds")
            webbrowser.open("https://ia904501.us.archive.org/31/items/war_worlds_solo_librivox/warofworlds_b1_ch01_wells_64kb.mp3")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}. by the way are you having a good time talking to me")
        elif 'bye' in query:
            speak("Bye sir, have a nice day")
            talk = False
        elif 'news' in query:
            news()
        elif 'are you there' in query:
            speak('no sir I am not there. I am here')
        elif 'your name' in query:
            speak("My Name is Jarvis, I am an Artificial Intelligence called as A I")
        elif 'email to me' in query:
            try:
                speak("What should I say? ")
                content = takeCommand()
                to = "put your gmail here" #put your gmail
                sendEmail(to, content)
                speak("Email has been sent")
                print("Email has been succesfully sent 😉")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send email at this moment")
        
