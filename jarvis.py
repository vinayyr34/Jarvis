import pyttsx3

# Initialize the engine once
engine = pyttsx3.init("sapi5")

def initialize_engine():
    # Set properties for the voice, rate, and volume
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set to the second voice (female)
    
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Decrease the rate of speech
    
    volume = engine.getProperty('volume')
    engine.setProperty('volume', min(volume + 0.25, 1.0))  # Increase volume but keep it within bounds
    
    return engine

# Call initialize_engine() to set properties once
initialize_engine()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("muchkond kuro bosudi bharath")
