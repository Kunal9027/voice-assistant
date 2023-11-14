from commands import *

def kunal():   
    wishMe()
    speak("how can i help you ?")
  
    while True:
                
        command = listen().lower() # it takes microphone input from the user and returns string output in lower case        

        if {"hello", "hi", "hey"} & set(command.split()):
            speak("Hello Sir, How can I help you?")
            
        
        elif {"time", "date"} & set(command.split()):
            now = datetime.datetime.now()
            speak("Current date and time : ")
            speak(now.strftime("%d-%m-%Y %H:%M:%S"))
        
        elif "search" in command:
            search()                
                
            
        elif "open brave" in command:
            brave()
          
        elif "close brave" in command:
            kill_brave()    
                
        elif 'youtube' in command:             # it open youtube
            youtue()
 
        elif 'open google' in command:              # it open google
            speak("Here you go to Google\n")
            search_url = f"https://www.google.com/"
            webbrowser.open("search_url")
 
        elif 'open stackoverflow' in command:         # it open stackoverflow
            stackoverflow()
            
        elif "wikipedia" in command:
           wikipedia()
            
            
        elif 'how are you' in command:
            speak("I am fine, Thank you sir")
            speak("How are you, Sir")
            
            if 'fine' in command or "good" in command:
                speak("It's good to know that your fine")
                
            elif 'i am sad' in command:
                speak("would you like to listen music ")
                
                if 'yes' in  command:
                    speak("hlo song")
 
        elif "wish me" in command:
            wishMe()
               
                
        elif {"about" , "who", "tell me about yourself"} & set(command.split()):
          #  print("I am a voice assistant created by the greatest enginner of all time. The one and only my mastre Kunal Chaudhary")
            speak("I am a voice assistant created by the greatest enginner of all time. The one and only my mastre Kunal Chaudhary")
        
        elif {"exit", "stop", "quit"} & set(command.split()):
            speak("Goodbye!")
            break