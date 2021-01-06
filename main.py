#variabels
UserInput = ""
ChatBot_Name = "zaki"
ChatBot_Name_Error = "console"
UserInput = str.lower(input("guest: "))
import pyfiglet
textascii = pyfiglet.figlet_format(":\ntest")

#Pesan
Pesan = ["hi", "your owner", "say", "ascii"]
respon = [": Hello guest.", ": you", ": not support", textascii]

#respon
if UserInput in Pesan:
	index = Pesan.index(UserInput)
	print(ChatBot_Name + respon[index])

if UserInput == "asciicus":
  asciicust = input(ChatBot_Name +": whats your text: ")
  asciicusto = pyfiglet.figlet_format(asciicust)
  print(ChatBot_Name + ":\n",asciicusto)

if UserInput == 'command':
  print(ChatBot_Name + ": ascii\nasciicus")

if UserInput == "":
  print(ChatBot_Name_Error + ": an error not found")