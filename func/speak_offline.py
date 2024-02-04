#pip install pyttsx3

import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#this will set speed for audio
engine.setProperty('rate', 150)
#this will set voice type
engine.setProperty('value', voices[0].id)

def Speak(*args, **kwargs):
    #here args and kwargs are used for any type of list input arguments or boolean
    audio = ""
    for i in args:
        audio += str(i)
    print(audio)
    engine.say(audio)
    engine.runAndWait()

#Speak("hello, my name is kartikeya")
    