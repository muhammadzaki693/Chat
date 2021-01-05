#variabels
UserInput = ""
ChatBot_Name = "zaki"
ChatBot_Name_Error = "Error"
UserInput = str.lower(input("guest: "))
import pyfiglet
textascii = pyfiglet.figlet_format(":\nsome text")
textlist = [
  "ascii"
  "random"
  "name"
]

#Pesan
Pesan = ["hi", "your owner", "", "say", "ascii"]
respon = [": Hello guest.", ": you", ": whats?", ": not support", textascii]

#respon
if UserInput in Pesan:
	index = Pesan.index(UserInput)
	print(ChatBot_Name + respon[index])

if UserInput not in Pesan:
	print(ChatBot_Name_Error + ': not found')