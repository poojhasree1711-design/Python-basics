import pyttsx3
engine=pyttsx3.init() #it starts the engine
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)-->male voice
engine.setProperty('voice', voices[1].id) #female voice
engine.say("Hello, this is my sample text") #gives the text to speak
engine.runAndWait() #executes it 