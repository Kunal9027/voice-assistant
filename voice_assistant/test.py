from voice import *
import speech_recognition as sr
import pyttsx3

def main():
    
    while True:
        
        command = listen().lower()
        
        if "wake up" in command :
            kunal()
            
        elif "kill all 001" in command:
            speak(" master command is accessed. system is shutting down")
            break
        
if __name__ == "__main__":
    main()