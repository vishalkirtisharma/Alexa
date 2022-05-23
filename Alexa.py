#  Windows logo key + R, type shell:startup,
# First Install below three require library

# pip install pyttsx3
# pip install PyAudio
# pip install SpeechRecognition
# pip install pywhatkit
# pip install wikipedia
# pip install pyjokes
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio use in case of error and install it via using Shift+Right click in powershell and then use pip install that file name

import pywhatkit
import speech_recognition as sr 
import pyttsx3 # test to speech
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import urllib


listener= sr.Recognizer()
engine= pyttsx3.init() # use for text to speech
voices=engine.getProperty('voices') # That one relate to product, we are using to change that voice id to female
engine.setProperty('voice',voices[1].id) # First once related to voice product then second one is varriable




# Create Function for various Purpose instead of repeat your code. 
def talk(text=f'  Hi {os.getlogin()}, What may i help you'): 
    engine.say(text)
    engine.runAndWait()



# Create function to take command from microphone and transfer to use this as a code.
def take_command(): 
    try:
        with sr.Microphone() as source:   
            print('Listening...')
            voice= listener.listen(source)
            command= listener.recognize_google(voice)
            command= command.lower()
            if 'alexa' in command:            
                command= command.replace('alexa','')
                
    except:
        command=''

    return command



def run_alex():
    while True:  

        command=take_command()
        if command == '':
            continue
        elif 'play' in command:
            song = command.replace('play','')
            talk(' Playing ' + song)
            print(' Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M  %p')
            print(time)
            talk('Current time is' + time)
        elif 'who is' in command:
            person  = command.replace('who is','')
            info= wikipedia.summary(person,1)
            print(info)
            talk(info)
        elif '''let's go for a date''' in command:
            talk(' Opps, I am already in relationship')
        elif 'are your single' in command:
            talk(' Hahaha,i am in relation with wifi. We have great day..')
        elif  'joke' in command:
            talk(pyjokes.get_joke())
        elif 'quit' in command or 'exit' in command:
            break
        elif ('shut down' in command or 'turn off' in command)  and ('computer' in command or 'system' in command):
            os.system('shutdown /s /t 1')
        
        elif ('restart' in command or 'turn off' in command)  and ('computer' in command or 'system' in command):
            os.system('shutdown /r /t 1')
        else:
            print(command+ "is not a valid . Please repate your command")
            talk(command + "is not a valid . Please repate your command")
        




try:
    talk() 
    run_alex()
except:
    print('''Seem you aren't connected right now.''')