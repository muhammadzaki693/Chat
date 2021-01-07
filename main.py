while (True):
	#var
	UserInput = ""
	ChatBot_Name = "zaki"
	ChatBot_Name_Error = "console"
	UserInput = str.lower(input("guest: "))
	import pyfiglet
	textascii = pyfiglet.figlet_format("\ntest")
	
	#say quit
	if UserInput == "quit" or UserInput == "end":
		print(ChatBot_Name + ": bye thanks use me")
		break
	
	if UserInput == "hi" or UserInput == "hello":
		print(ChatBot_Name + ": hello")
	elif UserInput == "your owner" or UserInput == "owner":
		print(
		    ChatBot_Name +
		    ": if you fork this project is your projects but official owner is muhamadzakirha"
		)
	elif UserInput == "ascii" or UserInput == "acii":
		print(ChatBot_Name + ":\n", textascii)
	else:
	  print(ChatBot_Name + ": whats sorry im not understand")
