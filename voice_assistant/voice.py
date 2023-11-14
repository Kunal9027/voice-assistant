from test import kunal
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):      
    engine.say(text)
    
    engine.runAndWait()

def listen():         
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source )
        audio = recognizer.listen(source)
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


def main():
    
    while True:
        
        command = listen().lower()
        
        if "wake up" in command :
            kunal()
           
        elif "kill all 001" in command:
            speak("master command accepted. voice assistant is shutting down")
            break
      
      

if __name__ == "__main__":
    main()
    