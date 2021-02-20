import speech_recognition
import pyttsx3
from datetime import date,datetime

engine = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening")
		audio = robot_ear.listen(mic)

	print("Robot: ...")	

	try:
	    you = robot_ear.recognize_google(audio)
	except:
	    you = ""  

	print("You:" + you)

	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello Bich Tram, Can i help you"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes, %S seconds")
	else: 
	    robot_brain = "I'm fine thank you" 	

	print("Robot: " + robot_brain)	

	engine.say(robot_brain)
	engine.runAndWait()