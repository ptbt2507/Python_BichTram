print("noi")

import pyttsx3

robot_brain = "Hello Bich Tram, Can I help you"

engine = pyttsx3.init()
engine.say(robot_brain)
engine.runAndWait()