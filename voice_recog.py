import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    mic = sr.Microphone(device_index=2)

    try:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print('Didnt quite catch that')




