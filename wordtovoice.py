import pyttsx3
a=pyttsx3.init()
b=input("Enter Your Word:")
a.say(b)
a.runAndWait()