
import wikipedia
import sys
import pyttsx




engine = pyttsx.init()
engine.setProperty('rate', 150)

variable = ""
while variable != 'quit':




	variable = raw_input('Lookup anything, type something in: ')

	engine.say(' Looked it up, I found . . .')
	test = wikipedia.summary(variable, sentences=2)
	print(test)
	engine.say(test)
	engine.runAndWait()

