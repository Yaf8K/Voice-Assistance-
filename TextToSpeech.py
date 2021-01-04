# using Library pyttsx3
#First I'll create an Instance

import pyttsx3 as p

engine = p.init()
volume = engine.getProperty("volume")
print(volume)
engine.say("Hello, how are you?")
engine.say("What would you like me to do?")

#voices = engine.getProperty("voices")
#engine.setProperty("voice", voices[0].id)
# 0 is for male voice
#1 is for female voice
#engine.say("what you mean")
engine.runAndWait()


