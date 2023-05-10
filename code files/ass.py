import pyttsx3 #for text to speech conversion
import datetime #to work with date and time
import speech_recognition as sr #translates spoken languages into text
import wikipedia #to make any search on wikipedia
import webbrowser #to allow displaying Web-based documents to users.
import os 
import pyjokes
import pyaudio
import wolframalpha
import time
import subprocess
import requests
import openai
from tkinter import*
import pywhatkit

openai.api_key = 'api key'
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    #give an audio respond "text to speech"
    engine.say(audio)
    engine.runAndWait()

def Wa(text):
    contacts = {"Karuna": "+919171212076","Mansi": "+917000716828","Fabin": "+919109044555","Mitushi Mam": "+918770907122"}
    pywhatkit.sendwhatmsg_instantly(phone_no=contacts["Karuna"], message=text,)

def wishMe():
    #here using date time module to wish acc to time
    hour = int(datetime.datetime.now().hour) 

    if hour>= 0 and hour<12: 
        speak("Good Morning  !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon  !")    
   
    else: 
        speak("Good Evening  !") 
    speak("i m  your assistent , how may i help you")  
    
def takeCommand():
    # taking command from user speech recognition
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 0.8
        audio = r.listen(source) 

    try:
        print("recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query} \n ")


    except Exception as e:
        print(e)
        speak("may i have your pardon please !")
        return "none"
        
    return query

def Chat_bot(message):
    messages = [
        {"role": "system", "content": "You are a kind helpful assistant."},]
    messages.append({"role": "user", "content": message},)
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

def assistant():
    while True:
        query = takeCommand().lower()

        # logic for executing query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'whatsapp message'in query:
            speak("who would you like to send message")
            name = takeCommand().lower()
            speak("what do you want to say")
            text = takeCommand().lower()
            speak("sending....")
            Wa(text)


        elif 'open youtube' in query:
            speak("please wait.....  opening youtube")
            webbrowser.open("https://www.youtube.com/user/YouTube/videos?app=desktop")
            time.sleep(5)


        elif 'can you sing' in query:
            speak("i can't sing but i can play a song for you...  here you go ")
            webbrowser.open("https://www.youtube.com/watch?v=OC6AFSZLtnk?")
            time.sleep(10)


        elif 'open google' in query:
            speak("please wait.....  opening google")
            webbrowser.open("https://www.google.com?app=desktop")
            time.sleep(5)

        elif 'close google' in query or 'close youtube' in query or 'close instagram' in query or 'close linkedin' in query or 'close all tabs'in query:
            speak("closing... ")
            os.system("TASKKILL /F /IM chrome.exe")
            
            time.sleep(2)

            

        elif 'open instagram' in query:
            speak("please wait.....  opening instagram")
            webbrowser.open("https://www.instagram.com?app=desktop")
            time.sleep(5)

        elif 'open linkedin' in query:
            speak("please wait.....  opening linkedin")
            webbrowser.open("https://linkedin.com?app=desktop") 
            time.sleep(2)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"time is {strTime}\n")
            speak(f"time is {strTime} \n")

        elif 'open code' in query:
            speak("please wait... opening code")
            codePath = "C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #target path in your pc
            os.startfile(codePath)
            time.sleep(5)

        elif "open gmail" in query:
            speak("please wait.....  opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox")
            time.sleep(5)


        elif 'open stack overflow' in query: 
            speak("Here you go to Stack Over flow.  Happy coding") 
            webbrowser.open("https://www.stackoverflow.com?app=desktop")
            time.sleep(5)

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(f"i got a good one for you listen {joke}")
        
        elif "write a note" in query: 
            speak("What should i write") 
            note = takeCommand() 
            file = open('note.txt', 'a') 
            file.write(note)
            speak("done!") 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("note.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
  
        elif "sleep" in query or "wait" in query:
            speak("i will be back in 2 min")
            time.sleep(120)
            speak("i am back at your service ")
        
        elif 'exit' in query or 'quit' in query: 
            speak("Shutting") 
            exit()
        elif(query):
            ans = Chat_bot(query)
            print(ans)
            speak(ans)

        else:
            app_id = "HAP288-HG8PPUWP6A"
            client = wolframalpha.Client(app_id) 
            res = client.query(query) 
            answer = next(res.results).text 
            print(answer)
            speak(answer)






root = Tk()
bg = PhotoImage(file = "WELCOME.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0) 
frame1 = Frame(root)
frame1.pack(pady = 20 )
root.title("AI assistant")
root.geometry('700x394')
btn = Button(root, text = "START" , fg = "red", command=assistant)
btn.place(x= 350,y=247)
wishMe()
root.mainloop()

            


        

        
            
          
        
        
            
