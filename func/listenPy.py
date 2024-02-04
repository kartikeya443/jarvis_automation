#pip install SpeechRecognition
#pip install PyAudio

import speech_recognition as sr

#initialising recognizer
recognizer = sr.Recognizer()

def Listen() -> str | None:
    #default mic source
    with sr.Microphone() as source:
        print("Listening...")
        
        #adjusting or ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        #listening to user input
        audio_data = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            
            #recognize speech using Google Search Recog
            text = recognizer.recognize_google(audio_data)
            print(f"Speech Recognized: {text}")
            return text
        
        except sr.UnknownValueError:
            print("Sorry, I am not able to process the audio.")
            return None
        
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None

#calling the function to recognize speech
recognized_text = Listen()        
