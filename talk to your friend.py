import pyttsx3
friend=pyttsx3.init()
speech=input("Enter something:")
friend.say(speech)
friend.save_to_file(speech, "test.mp3")
friend.runAndWait()