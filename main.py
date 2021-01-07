while (True):
	#var
	UserInput = ""
	ChatBot_Name = "zaki"
	ChatBot_Name_Error = "console"
	UserInput = str.lower(input("guest: "))
	import pyfiglet
	textascii = pyfiglet.figlet_format("\ntest")

	if UserInput == "hi":
		print(ChatBot_Name + ": hello")
	elif UserInput == "your owner":
		print(
		    ChatBot_Name +
		    ": if you fork this project is your projects but official owner is muhamadzakirha"
		)
	elif UserInput == "say":
		print(ChatBot_Name + ": ", UserInput)
	elif UserInput == "ascii":
		print(ChatBot_Name + ":\n", textascii)
	elif UserInput == "quit":
		print(ChatBot_Name + ": bye thanks use me")
		break
