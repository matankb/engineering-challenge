import speech_recognition as sr

rec = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
  #calibrates for background noise
  rec.adjust_for_ambient_noise(source)

#def phrase_heard(rec, audio):
  #try:
    #sr_onsuccess(rec.recognize_google(audio))
  #except Exception as e:
    #sr_onfailure(e)

#rec.listen_in_background(mic, phrase_heard)
