import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary  # Ensure this module is correctly defined

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open whatsapp" in c:
        webbrowser.open("https://whatsapp.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.split(" ", 1)[1]  # Get the song name
        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Song not found.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio).lower()

                if word == "jarvis":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Jarvis Active... Listening for command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)

                        processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("Speech Recognition service is unavailable")
        except Exception as e:
            print(f"Error: {e}")
