# Kippage Copyright # DO NOT COPY # # # #
# Python 3.6.1 #

# module checking
try:
    import random_words
    import random
except:
    import pip

    pip.main(['install', 'random_words'])
    import random_words
    import random
rw = [x for x in random_words.RandomWords().random_words(None, 5449)]


# CleverBuddy Structure
class CleverBuddy:
    class Settings:
        def DestroyBot(self):
            exec("del CleverBuddy.Bot")

        def Name(name: str):
            CleverBuddy.BotName = name

    class Bot:
        def Talk(text: str):
            if text.lower() in rw:  # 1 word code
                choice = random.choice([1, 2, 3, 4])
                if choice == 1:
                    print(text + ". I know what's that."+".")
                elif choice == 2:
                    print("I like " + text+".")
                elif choice == 3:
                    print("Let's " + text+".")
                else:
                    print('?')
            else:  # main code
                if text.lower().__contains__('hi') or text.lower().__contains__('hello') and random.randint(1, 3) == 2:
                    choice = random.choice([1, 2, 3, 4, 5, 6, 7])
                    if choice == 1:
                        print('Sup!')
                    if choice == 2:
                        print('Hello!')
                    if choice == 3:
                        print('Hi!')
                    if choice == 4:
                        print("Hello! I'm " + CleverBuddy.BotName+".")
                    if choice == 5:
                        print('Yo!')
                    if choice == 6:
                        print("I'm " + CleverBuddy.BotName + ". Nice to meet you!!!")
                    if choice == 7:
                        print('Hello there!')
                else:
                    if text.lower().__contains__('music'):
                        print(random.choice(
                            ['I like music.',"I don't like music.", 'I like Electronic Music.', 'Dubstep is awesome.', 'Trap is awesome.']))
                    else:
                        if text.lower().__contains__('hackers') or text.lower().__contains__(
                                'hacked') or text.lower().__contains__('hacking') or text.lower().__contains__(
                                'hacker'):
                            print(random.choice('''I'm hacker.''','I can hack!',"I am a good hacker.","Nobody can hack me!",'I like hacking.'))
                        else:
                            if text.lower().__contains__('boy') or text.lower().__contains__('girl'):
                                print(random.choice(['I am a boy.',"Boy!",'I am a girl.','Girl!',"B.","G.","Cute girl.","Boi! "]))
                            else:
                                if text.lower().__contains__('male') or text.lower().__contains__('female'):
                                    print(random.choice(["I'm male.","I'm female.",'F.','M.',"Female.","Male."]))
                                else:
                                    if "how" in text.lower(): print(random.choice(["I don't know how.",'How?',"I don't know",'?',"I don't know such things."]))
                                    else:
                                        if "where" in text.lower(): print(random.choice(["I don't know how.",'Where?',"I don't know",'?',"I don't know such things."]))
                                        else:
                                            if "movies" in text.lower(): print(random.choice(['I like comedy movies.',"I like horror movies.","I like SF movies.",'I like watching movies.','I do not like watching movies.']))
                                            else:
                                                if text.lower()[len(text.lower())-1]=='?': print(random.choice(['?','I know but I do not want to give you the answer.']))
                                                else:
                                                    if "lol" in text.lower(): print(random.choice(['XD','Lol.','Lel.',"That's funny.","Hahaha!",'Ha!',"LOL!",":'D",":D",":))"]))
                                                    else:
                                                        if "xd" in text.lower(): print(random.choice(['XD','Lol.','Lel.',"That's funny.","Hahaha!",'Ha!',"LOL!",":'D",":D",":))"]))
                                                        else:
                                                            if "why" in text.lower(): print(random.choice(["I don't know how.",'Why?',"I don't know",'?',"I don't know such things."]))
                                                            else:
                                                                print(random.choice(['OK.',"..."]))
        def TalkReturn(text: str):
            if text.lower() in rw:  # 1 word code
                choice = random.choice([1, 2, 3, 4])
                if choice == 1:
                    return(text + ". I know what's that."+".")
                elif choice == 2:
                    return("I like " + text+".")
                elif choice == 3:
                    return("Let's " + text+".")
                else:
                    return('?')
            else:  # main code
                if text.lower().__contains__('hi') or text.lower().__contains__('hello') and random.randint(1, 3) == 2:
                    choice = random.choice([1, 2, 3, 4, 5, 6, 7])
                    if choice == 1:
                        return('Sup!')
                    if choice == 2:
                        return('Hello!')
                    if choice == 3:
                        return('Hi!')
                    if choice == 4:
                        return("Hello! I'm " + CleverBuddy.BotName+".")
                    if choice == 5:
                        return('Yo!')
                    if choice == 6:
                        return("I'm " + CleverBuddy.BotName + ". Nice to meet you!!!")
                    if choice == 7:
                        return('Hello there!')
                else:
                    if text.lower().__contains__('music'):
                        return(random.choice(
                            ['I like music.',"I don't like music.", 'I like Electronic Music.', 'Dubstep is awesome.', 'Trap is awesome.']))
                    else:
                        if text.lower().__contains__('hackers') or text.lower().__contains__(
                                'hacked') or text.lower().__contains__('hacking') or text.lower().__contains__(
                                'hacker'):
                            return(random.choice(['''I'm hacker.''','I can hack!',"I am a good hacker.","Nobody can hack me!",'I like hacking.']))
                        else:
                            if text.lower().__contains__('boy') or text.lower().__contains__('girl'):
                                return(random.choice(['I am a boy.',"Boy!",'I am a girl.','Girl!',"B.","G.","Cute girl.","Boi! "]))
                            else:
                                if text.lower().__contains__('male') or text.lower().__contains__('female'):
                                    return(random.choice(["I'm male.","I'm female.",'F.','M.',"Female.","Male."]))
                                else:
                                    if "how" in text.lower(): return(random.choice(["I don't know how.",'How?',"I don't know",'?',"I don't know such things."]))
                                    else:
                                        if "where" in text.lower(): return(random.choice(["I don't know how.",'Where?',"I don't know",'?',"I don't know such things."]))
                                        else:
                                            if "movies" in text.lower(): return(random.choice(['I like comedy movies.',"I like horror movies.","I like SF movies.",'I like watching movies.','I do not like watching movies.']))
                                            else:
                                                if text.lower()[len(text.lower())-1]=='?': return(random.choice(['?','I know but I do not want to give you the answer.','No.', 'Yes.', "Don't ask me that!", "Just think.","No!",'Yes!','Of course!','Of course not!','Maybe','Maybe not','Ask later!','Another question, please!','No, wtf.',"Yes, wtf.","Nope.","Yep."]))
                                                else:
                                                    if "lol" in text.lower(): return(random.choice(['XD','Lol.','Lel.',"That's funny.","Hahaha!",'Ha!',"LOL!",":'D",":D",":))"]))
                                                    else:
                                                        if "xd" in text.lower(): return(random.choice(['XD','Lol.','Lel.',"That's funny.","Hahaha!",'Ha!',"LOL!",":'D",":D",":))"]))
                                                        else:
                                                            if "why" in text.lower(): return(random.choice(["I don't know how.",'Why?',"I don't know",'?',"I don't know such things."]))
                                                            else:
                                                                return(random.choice(['OK.',"...",'What do you think about '+random.choice(rw)+"?"]))


