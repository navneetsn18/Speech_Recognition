import speech_recognition as speech 

rec=speech.Recognizer()

with speech.Microphone() as source:
    print("Please say something: ")
    audio=rec.listen(source)
    try:
        result=rec.recognize_google(audio)
        print("You just said: {}".format(result))
    except:
        print("Sorry! Unable to understand what you just said.")
    
