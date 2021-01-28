import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit


#initializing the modules
s= sr.Recognizer()
p= pyttsx3.init()
#changing the voice
voice= p.getProperty("voices")
p.setProperty("voice",voice[1].id)
#p.setProperty("rate", 120)
p.setProperty("volume",1)
p.runAndWait()
#initialization done




#speech to text
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            global m
            m= r.recognize_google(audio)
            m= m.lower()

            print(m)
        except Exception as e:
            print(e)
            m=""
    return "none"



#speak
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate",150)
    engine.say(audio)
    engine.runAndWait()


#opening the websites
#it is called form the infinity function
#idk what to write
def open():
    if "google" in m:
        webbrowser.open("www.google.com")

        exit()

    if "youtube" in m:
        webbrowser.open("www.youtube.com")
        exit()



def hello():
    speech()
    global request
    request=m
    if "mona" in m:
        infinity()





#main loop
#it is an infinite loop
def infinity():

    speak("hello baby ")
    speak("how u doing")
    speak("so how may i help you ")




    while True:

        speech()
        # search
        searchlist = ["what", "who", "where", "how", "whom", "recommend", "suggenst"]
        youtubelist = ["play", "youtube"]

        if "open" in m:
            open()
        if "bye" in m:
            speak("bye baby take care")
            exit()
        for i in youtubelist :
            if i in m:
                speak("opening youtube")
                pywhatkit.playonyt(m)

        for i in searchlist:
            if i in m:
                speak("opening google")
                pywhatkit.search(m)


hello()











