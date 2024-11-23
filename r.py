import pyttsx3
for i in range(2):
    engine = pyttsx3.init()
    text= "happy birthday to you happy birthday to you happy birthday dear one happy birthday to you                       may god bless you may god bless you may gog bless you dear one happy birthday TO you"
    engine.say(text)

    engine.runAndWait()