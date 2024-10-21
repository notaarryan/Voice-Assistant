import speech_recognition as sr
import webbrowser
import pyttsx3
import music

artists = []

for keys in music.artistURI:
    artists.append(keys)

engine = pyttsx3.init()
engine.setProperty('rate',150)

def getArtistId(artist):
    pass


def open(command):
    if "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open my github profile" in command.lower():
        webbrowser.open("https://github.com/notaarryan")
    elif "open instagram" in command.lower():
        webbrowser.open("https://instagram.com")
    elif "open my linkedin profile" in command.lower():
        webbrowser.open("https://www.linkedin.com/in/aryan-parmar-a0634b299/")

def playMusic(command):
    if "play music" in command.lower():
        webbrowser.open("https://open.spotify.com/")
    for artist in artists:
        if f"play {artist}" in command.lower():
            webbrowser.open(f"https://open.spotify.com/artist/{music.artistURI[artist]}")


def process(command):
    if "play" in command.lower():
        playMusic(command)

    if "open" in command.lower():
        open(command)


def speak(text :str):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
if __name__ == "__main__":
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            wake = r.recognize_google(audio)
            if wake.lower() == "hey assistant":
                speak("Hello")
                with sr.Microphone() as source:
                    print("Assistant Listening...")
                    audio = r.listen(source,timeout=4,phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    process(command)
        except Exception as e:
            print(f"Error {e}")