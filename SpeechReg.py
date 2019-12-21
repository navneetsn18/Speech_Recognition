import speech_recognition as speech

rec=speech.Recognizer()

with speech.Microphone() as source:
    print("Please speak something: ")
    audio=rec.listen(source)
    try:
        result=rec.recorgnize_google(audio)
        print("You just said: {}".format(result))
    except:
        print("Sorry! Unable to understand what you jsut said!")