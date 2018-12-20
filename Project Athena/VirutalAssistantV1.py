import pyttsx3

engine = pyttsx3.init()
engine.say('Hello World')
engine.setProperty('rate', 100)
engine.runAndWait()