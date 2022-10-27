import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'brian' in command:
                command=command.replace('brian','')
                talk(command)
    except:
        pass
    return command

def run_brian():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' +time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('I am fine What about you?')
    elif 'who is your girlfriend?' in command:
        talk('Wifi')
    elif 'who is your favorite person' in command:
        talk('Abishek is my favorite person')
    elif 'who created you' in command:
        talk('Abishek')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


run_brian()