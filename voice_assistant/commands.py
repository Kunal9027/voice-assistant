#------IMPORTING REQUIRED MODULES------#
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os


#------INITIALIZING MODULES & FUNCTIONS------#

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):      #speak function
    engine.say(text)
    
    engine.runAndWait()

def listen():         #listen function
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source )
        audio = recognizer.listen(source)
        print("Recognizing...")
        
        
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results: {e}")
            return ""

#------ MAIN FEATURES ------#

def wishMe():         #wish me function
    
    hour = int(datetime.datetime.now().hour)
    if hour>= 6 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<16:
        speak("Good Afternoon Sir !")   
  
    else:
        speak("Good Evening Sir !")
       
def youtue_search():         #youtube search function
    while True:
        speak("what should i search on youtube")
        query = listen()
        if query:
            search_url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(search_url)
            speak(f"Here are the search results for '{query}'.")
            break 

def open_youtube():
    speak("opening youtube")
    search_url = f"https://www.youtube.com/"
    webbrowser.open(search_url)
        
def brave():           #brave browser open function
    speak("opening brave")
    os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
  
def kill_brave():      #brave browser close function
    speak("closing brave")
    os.system("taskkill /f /im brave.exe")     
        
def search():          #google search function  
    while True:
        
        speak("what should i search on google")
        query = listen()
        if query:
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            speak(f"Here are the search results for '{query}'.")
            break

def open_google():     #open google search function
    speak("opening google")
    search_url = f"https://www.google.com/"
    webbrowser.open(search_url)        
                       
def stackoverflow():    #open stackoverflow search function
    speak("Here you go to Stack Over flow. Happy coding")
    search_url = f"https://www.stackoverflow.com/"
    webbrowser.open(search_url)     
        
def wikipedia():       #open wikipedia search function
    speak("Here you go to wikipedia")
    search_url = f"https://www.wikipedia.com/"
    webbrowser.open(search_url)      
        
def edge():            #open edge browser search function
    speak("opening edge")
    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    
def kill_edge():       #close edge browser search function
    speak("closing edge")
    os.system("taskkill /f /im msedge.exe")
    
def notepad():         #open notepad function
    speak("opening notepad")
    os.startfile("C:\\Windows\\System32\\notepad.exe")    
    
def kill_notepad():    #close notepad function
    speak("closing notepad")
    os.system("taskkill /f /im notepad.exe")
    

 
 
    
    
    