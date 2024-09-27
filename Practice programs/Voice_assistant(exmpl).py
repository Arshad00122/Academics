import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
	engine.say(audio) # Engine would say audio
	engine.runAndWait()


def wishMe():
	hour=int(datetime.datetime.now().hour)

	if hour>=0 and hour<=12:
		speak("Good morning!")

	elif hour>=12 and hour<=18:
		speak("Good Afternoon!")	

	else:
		speak("Good evening!")

	speak("It's your assistant Jarvis")
	speak("How can i help you?")

def takeCommand():
	#It takes mic input and returns string output

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print ("listening....")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print ("Recognizing...")
		query = r.recognize_google(audio, language = "en-in")
		print (f"User said:{query}\n")

	except Exception as e:
		# print (e)
		print ("say that again please....")
		speak ("say that again please....")

		return "None"
	return query

def hola():
	greeting_lst=["Hello","Hola Amigo","Yes?"]
	hello=random.choice(greeting_lst)
	speak(hello)

def bye():
	quit_lst=["Adios","Good bye","have a nice day"]
	bye=random.choice(quit_lst)
	speak(bye)

if __name__ == "__main__": # To check if the file is being imported or directly run in jarvin.py
	#wishMe()
	while True:
		query = takeCommand().lower()

		if "repeat" in query:
			speak(query)

		elif "wikipedia" in query:
			speak("searching wikipedia...")
			query = query.replace('wikipedia',"")
			results = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			print(results)
			speak(results)
		
		elif "open youtube" in query:
			webbrowser.open("youtube.com")
			
		elif "open google" in query:
			webbrowser.open("google.com")
		
		elif "play music" in query:
			music_dir ='C:\\Users\\ARSHAD ALI\\Music\\Songs downloaded'
			songs = os.listdir(music_dir)
			print (songs)
			os.startfile(os.path.join(music_dir, songs[1]))
		
		elif "bye-bye" in query:
			bye()
			break

		elif "hello" in query:
			hola()
			speak("I am your assistant Jarvis")

		elif "time" in query:
			timestr=datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"The time is {timestr}")
			speak("Have a great day!")

		elif "what can you do" in query:
			speak("I can do many things like opening google,")
			speak("youtube and even play music for you")
