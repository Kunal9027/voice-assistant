import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source )
        audio = recognizer.listen(source, )
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

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 6 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<16:
        speak("Good Afternoon Sir !")   
  
    else:
        speak("Good Evening Sir !")

def create_reminder(reminder_text, time):
    # You can implement this function to create reminders using a calendar API or file storage
    # For simplicity, we will just print the reminder here
    print(f"Reminder: '{reminder_text}' set for {time}.")

def create_todo_list(task_text):
    # You can implement this function to add tasks to a to-do list using a task management library or file storage
    # For simplicity, we will just print the task here
    print(f"Added to your to-do list: '{task_text}'.")

def kunal():
    
    wishMe()
    speak("how can i help you ?")
   
    
    while True:
                
        #speak("What can I do for you?")   if listen is geater than 1 time then it speak this line
        
        command = listen().lower()
        
        
        if "reminder" in command:
            speak("What should I remind you about?")
            reminder_text = listen()
            if reminder_text:
                speak("When should I remind you?")
                reminder_time = listen()
                create_reminder(reminder_text, reminder_time)
                speak(f"Reminder set for {reminder_time}.")
        
        elif "to-do list" in command:
            speak("What task would you like to add to your to-do list?")
            task_text = listen()
            if task_text:
                create_todo_list(task_text)
                speak(f"Task '{task_text}' added to your to-do list.")
        
        elif "search" in command:
            speak("What would you like to search for?")
            query = listen()
            if query:
                search_url = f"https://www.google.com/search?q={query}"
                webbrowser.open(search_url)
                speak(f"Here are the search results for '{query}'.")
                
                
        elif 'open youtube' in command:             # it open youtube
            speak("what should i search on youtube")
            query = listen()
            if query:
                search_url = f"https://www.youtube.com/results?search_query={query}"
                webbrowser.open(search_url)
                speak(f"Here are the search results for '{query}'.")
 
        elif 'open google' in command:              # it open google
            speak("Here you go to Google\n")
            search_url = f"https://www.google.com/"
            webbrowser.open("search_url")
 
        elif 'open stackoverflow' in command:         # it open stackoverflow
            speak("Here you go to Stack Over flow.Happy coding")
            search_url = f"https://www.stackoverflow.com/"
            webbrowser.open(search_url)
            
        elif "wikipedia" in command:
            search_url = f"https://www.wikipedia.com/"
            webbrowser.open(search_url)
            
            
        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            
            if 'fine' in command or "good" in command:
                speak("It's good to know that your fine")
                
            elif 'i am sad' in command:
                speak("would you like to listen music ")
                
                if 'yes' in  command:
                    
            
            
        elif "where is" in command:              
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
            
 
        elif "kunal" in command:
            wishMe()
        
                
                
        elif {"about" , "who are you", "tell me about yourself"} & set(command.split()):
            print("I am a voice assistant created by the greatest enginner of all time. The one and only my mastre Kunal Chaudhary")
            speak("I am a voice assistant created by the greatest enginner of all time. The one and only my mastre Kunal Chaudhary")
        
        elif {"exit", "stop", "quit"} & set(command.split()):
            speak("Goodbye!")
            break

