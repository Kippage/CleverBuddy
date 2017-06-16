import CleverBuddy
CleverBuddy.CleverBuddy.Settings.Name('Bot')
talk = lambda x: CleverBuddy.CleverBuddy.Bot.TalkReturn(x)
while 1:
	user=input("> ")
	if user!="":
		print(talk(str(user)))	
