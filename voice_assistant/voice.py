from test import *


def main():
    
    
    while True:
        print("Say wake up to wake up the voice assistant")
        
        command = listen().lower()
        

        if "wake up" in command :
            kunal()
           
        elif "kill all 001" in command:
            speak("master command accepted. voice assistant is shutting down")
            break
      
      

if __name__ == "__main__":
    main()
