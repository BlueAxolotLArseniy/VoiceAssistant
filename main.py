import time
import speech_recognition as sr
import pyttsx3 as pysx
import sys as sus
import os

questions = {'welcome': ('привет',),
             'farewell': ('пока', 'до встречи', 'увидимся',),
             'tasks': {
                 'calc': ('запусти калькулятор', 'включи калькулятор', 'открой калькулятор'),
             }}

def speak(msg):
    print(msg)
    speak_engine.say(msg)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(reg, audio):
    global truee
    try:
        voice = reg.recognize_google(audio, language='ru-Ru')
        print('[log] Распознано: ' + voice)
        
        for i in questions['farewell']:
            if i in voice.lower():
                print('[log] Программа завершена!')
                truee = False
                sus.exit()
        for i in questions['tasks']['calc']:
            if i in voice.lower():
                print('[log] Запуск калькулятора!')
                os.system('calc')
            
    except sr.UnknownValueError:
        print('[log] Голос не распознан!')
    except sr.RequestError as e:
        print('[log] Неизвестная ошибка, проверьте интернет!')

r = sr.Recognizer()
speak_engine = pysx.init()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak('Добрый день, повелитель')
speak('Астра слушает')

truee = True
stop_listening = r.listen_in_background(m, callback)
while truee: time.sleep(0.1)