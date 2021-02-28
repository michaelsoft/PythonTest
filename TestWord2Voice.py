#coding: UTF-8
import pyttsx3

engine = pyttsx3.init()
#engine.say("Hello Wayne!")
#engine.setProperty('voice', 'zh')
engine.say(U'轻轻地，我走了')
engine.runAndWait()