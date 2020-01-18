# -*- coding: utf-8 -*-
"""
Created on

@author: Lonewolf
"""
import speech_recognition as sr

def speech_command_text():
    r = sr.Recognizer()
   
    with sr.Microphone() as source:
        print("Say Somthing")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
       
       
    try:
        print(r.recognize_google(audio))
        text = r.recognize_google(audio)
        print("Times over thanks")
    except:
        pass;
    return text
text = speech_command_text()
print(text)

