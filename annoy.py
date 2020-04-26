from pynput.keyboard import Key, Controller
import time
import urllib2

keyboard = Controller()

f = urllib2.urlopen("https://gist.githubusercontent.com/rudydelorenzo/04109cb8ea7361f17c33e9d8cf2abb4c/raw/")
script = f.read()

scriptlines = script.split("\n\n  \n")

lines = []
for line in scriptlines:
	lines.append(line.replace("\n", " "))

time.sleep(3)

for line in lines:
	for char in line:
		keyboard.press(char)
		keyboard.release(char)
		time.sleep(0.03)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	#Sleep might be necessary for cetain applications
	#time.sleep(0.2)