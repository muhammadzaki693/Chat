
#variabels
UserInput = ""
ChatBot_Name = "zaki"
ChatBot_Name_Error = "Error"
UserInput = str.lower(input("guest: "))

#Pesan
Pesan = ["hi", "your owner", "", "say"]
respon = [": Hello guest.", ": you", ": whats?", ": not support"]

#respon
if UserInput in Pesan:
	index = Pesan.index(UserInput)
	print(ChatBot_Name + respon[index])

if UserInput not in Pesan:
	print(ChatBot_Name_Error + ': not found')