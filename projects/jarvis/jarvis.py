# -*- coding: utf-8 -*-
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os





engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    #from win32.client import Dispatch
    #speak = Dispatch("SAPI.SpVoice")
    #speak.Speak(audio)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning yash!")
    elif hour>=12 and hour<18:
        speak("good afternoon yash!")
    else:
        speak("good evening yash")
    
    speak("I am jarvis. how may i help you")

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("pls say something i am listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
        
        
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")  
        
        
    except Exception as e:
       # print(e)
        print("say again please..")
        return "none"
    return query

#def sendEmail(to,content):
    
        
if __name__ == '__main__' :
    speak(" HI YASH how are you")
    wishMe()
    
    
    while True:
        query=takeCommand().lower()
        
        if'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)  
            speak(results)
        elif 'what is my name' in query:
            speak("sir,your name is Yash")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open cc' in query:
            webbrowser.open("https://www.codechef.com/")
        elif 'open cf' in query:
            webbrowser.open("https://codeforces.com/")
        elif 'open gaana' in query :
            webbrowser.open("gaana.com")
        elif 'time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Yash U Hegde\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open books' in query:
            bookPath = "D://yash documents//yash books"
            os.startfile(bookPath) 
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/feed/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif ' jasmine stop' in query :
            exit()
        
        '''elif 'email ' in query :
            try:
                speak("what should i say?")
                content = takeCommand()
                to = takeCommand()
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e :
                print(e)
                speak("unable to send")'''
                
         
    
    
    
     

