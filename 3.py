import pyttsx3


# initialize Text-to-speech engine
engine = pyttsx3.init()


# convert this text to speech
for i in range(5):
    text = "i love you mummy"
    print(f"{text} ☺☺ ")
    engine.say(text)
    # play the speech
    engine.runAndWait()