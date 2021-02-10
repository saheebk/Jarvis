from google import google
import requests, sys, bs4

import webbrowser
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:



        print("Listening...")
        audio=r.listen(source)

    try:

        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n" )
    except Exception as a:
        print("")
        return "None"
    return query
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good   Evening")
    speak("How may I help you Sir!?")
name="Saheeb"
if __name__=="__main__":
    while True:
        query= takeCommand().lower()
        if 'jelly' in query:
            wishme()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace('wikipedia', "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open netflix' in query:
            webbrowser.open('netflix.com')
      
        elif 'search' in query:
            num_page = 1
            search_results = google.search(query, num_page)
            for result in search_results:

                webbrowser.open(result.name)
        elif 'that is not my name' in query:
            speak("ok what is your name?")
        elif 'my name is'  in query:
            speak("Ok, I'll remember that sir")
        
        elif 'exit jelly' in query:
            speak("Ok! Goodbye ! "+name)
            exit()
        elif 'play music' in query:
            webbrowser.open('https://www.youtube.com/watch?v=yA6W2pOi3XY')
        elif 'who are you' in query:
            speak("I am JellyBean, a personal assistant software")



           # result=search(query, num_results=1)
            #print(result)
            #webbrowser.open('https://www.youtube.com/watch?v=Lp9Ftuq2sVI')

