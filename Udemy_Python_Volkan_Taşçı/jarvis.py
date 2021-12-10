from banka_uygulaması import *

#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import os
import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    os.system("cls")
    print("Say something!")
    audio = r.listen(source)

flag = False

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text =r.recognize_google(audio, language ="tr") # Türkçeye çevirmek için virgül ekleyip language = "tr" ibaresi koyuyoruz.
    print("Algılanan: " + text)
    flag = True
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

if flag:
    if text == "program çalıştır":
        main()


