import speech_recognition as sr

rec = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
  #calibrates for background noise
  rec.adjust_for_ambient_noise(source)

def start_listening(onsuccess, onfailure):
    def phrase_heard(rec, audio):
        try:
            onsuccess(rec.recognize_google)
        except Exception as e:
            onfailure(e)
    rec.listen_in_background(mic, phrase_heard)
