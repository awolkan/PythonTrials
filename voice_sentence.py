# include pyttsx3
import pyttsx3


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Text to be spoken
text = "Hello! I am a Python program speaking to you."

# Speak the text
engine.say(text)
engine.runAndWait()