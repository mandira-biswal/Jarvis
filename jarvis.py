import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# WishMe function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I assist you today?")

# Function to get current time
def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

# TakeCommand function
def takeCommand():
    # Initialize the recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query:
            query = query.lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia:")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("There were multiple results; please be more specific.")
                    print(e.options)
                except wikipedia.exceptions.HTTPTimeoutError:
                    speak("The request to Wikipedia timed out; please try again later.")
                except Exception as e:
                    speak("An error occurred while fetching Wikipedia results.")
                    print(e)
        
            elif 'open youtube' in query:
                speak('Opening YouTube...')
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in query:
                speak('Opening Google...')
                webbrowser.open("https://www.google.com")
            
           
            elif 'the time' in query:
                current_time = get_current_time()
                speak(f"The current time is {current_time}")
                print(f"The current time is {current_time}")
