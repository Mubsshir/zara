import pyttsx3
import getpass
import random
import os
import pyttsx3 
import speech_recognition as sr
import sys
import datetime
import wikipedia
import webbrowser

#pwd=getpass.getpass("password: ")

def clear():
	
	if os.name=='nt':
		_=os.system('cls')
	
	else:
		_=os.system('clear')
	
	pass

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):

	engine.say(audio)

	engine.runAndWait()

	pass

def wishme():

	hour=datetime.datetime.now().hour

	if hour<=0 and hour<12:
		speak('Good Morning')

	elif hour<=12 and hour<18:
		speak('good afternoon')

	else:
		speak('good evening')
	speak("My Name is Zara, How may I help you")
	pass

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening.................")
		r.pause_threshold=1
		audio=r.listen(source)
		#We have successfully created our takeCommand() function.
		# Now we are going to add a try and except block to our program to handle errors effectively.
		try:
			print("Recognizing.......")
			quary=r.recognize_google(audio,language='en-in')
			print(f"user said={quary}")

		except Exception as e:
			print(e)
			print("Say That again! please")
			return 'None'
	return quary


if __name__=="__main__":
	clear()
	wishme()
	while True:
		
		quary=takeCommand().lower()
		if "wikipedia" in quary:
			quary.replace("wikipedia",'')
			results=wikipedia.summary(quary,sentences='2')
			speak(results)
		
		elif "open youtube" in quary:
			webbrowser.open("www.youtube.com")
		
		elif "open google" in quary:
			webbrowser.open("www.google.com")
		
		elif "play song" in quary:
			SongDir='D:\SONG'
			songs=os.listdir(SongDir)
			numberOFsong=len(songs)
			rsong=random.randint(0,numberOFsong)
			os.startfile(os.path.join(SongDir,songs[rsong]))
		
		elif "the time" in quary:
			currentTime=datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"the time is {currentTime}")
		
		elif 'close' or 'exit' or 'bnd ho ja' in quary:
			sys.exit()
