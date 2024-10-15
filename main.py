import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',150)

def speak(text :str):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
if __name__ == "__main__":
    speak("Voice Asistant Active")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Voice Asistant is Listening")
            try:
                audio = r.listen(source,timeout=4)
                try:
                    command = r.recognize_google(audio)
                    print(command)
                except sr.UnknownValueError:
                    print("Voice Assistant could not understand audio")
                except Exception:
                    speak("I am sorry I could not hear you")
            except sr.exceptions.WaitTimeoutError:
                speak("I am sorry I could not hear you")
        