import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes

engine = pyttsx3.init()    #here we are putting python text-to-speech convertor in 'engine' variable
voices = engine.getProperty('voices')    #here we get the voices present in the pyttsx3 and put them in 'voices
engine.setProperty('voice', voices[1].id)  #here we set the '1' index value voice in the engine as our default voice 

#the function below talks in the voice we decided above(right now female voice) 
def talk(text):
    engine.say(text)    #this command is used to talk or repeat the words said by the user
    engine.runAndWait()  #i'm guessing this command is to run and wait for a certain amount of time


listener = sr.Recognizer()   #this is the speech recogniser

def taking_command():
    try:
        with sr.Microphone() as source:    #here using sr.Microphone we declare it as a source of audio 
           print("Listening....")
           voice = listener.listen(source)    #now the listener listen's to the source
           cmd = listener.recognize_google(voice)    #this recognize_google command converts voice to text using google
           cmd = cmd.lower()
           if "alexa" in cmd:
              cmd = cmd.replace('alexa', '')
              print(cmd)
              #talk(cmd)

    except:   
        pass 
    return cmd

def run_cmd():
    cmd = taking_command()  #here we call the taking_command() function in the cmd variable 
    if 'play' in cmd:
        song = cmd.replace('play', '')   #we replace the word play from the cmd 
        talk("Playing " + song)   
        pywhatkit.playonyt(song)   #this command searches and plays whatever cmd we give on youtube
    elif 'time' in cmd:
        time =  datetime.datetime.now().strftime('%H:%M %p')     #cmd to get current time in 24hr format and with AM/PM
        talk("Current time is " + time)  
    elif 'search' in cmd:
        srch = cmd.replace('search', '')
        info = wikipedia.summary(srch, 2)   #this cmd gives us the wikipedia search of whatever we ask it for, and it is given here 2 attributes first is the cmd to be searched and the 2nd is the number of lines we wanna get from the search
        talk(info)    
    elif 'joke' in cmd:
        talk(pyjokes.get_joke())    #this cmd tells us a joke
    else:
        talk('Can you please repeat for me?')    

run_cmd()