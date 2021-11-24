import random
name=input("Pls enter your name: ")
print("helloo",name.upper(),"welcome to the hangman game!!\nTo read the rules of this game,type rules\nTo start the game directly,type start\nTo exit the game,type exit")
n=input()
p=n.lower()
store=""
sb={"fruits":("strawberry","banana","apple","orange","guava","grapes"),"colours":("red","blue","orange","brown","yellow"),"cars":("maruti","nano","ferrrari","audi","jaguar")}
keys=list(sb)
for i in range(len(keys)):
    f=random.randint(0,len(keys)-1)
    j=keys[f]
    q=sb[j]
    r=random.randint(0,len(q)-1)
    x=q[r]
if p!="start" and p!="rules" and p!="exit":
    print("oops!!wrong command!!enter the command again pls!!")
    cc=input("Enter the CORRECT command in pls: ")
    store=cc.lower()
if p=="start" or store=="start":
    print("Seems like you know the rules of the game already!!let's start then...")
    action=input("To start the game pls type confirm, to read the rules once pls type rules:\n")
    if action=="rules":
        print("SO THE HANGMAN GAME IS A REALLY SIMPLE GAME\nHere, a random word is picked up from our collection and the player gets limited chances to win the game.")
        print("When a letter in that word is guessed correctly, that letter position in the word is made visible.\nIn this way, all letters of the word are to be guessed before all the chances are over.\nIn other word, I have a secret list of fruits for me,you have to guess the correct fruit")
        print("You shall be getting only 2 MORE GUESSES than the total number of alphabets in the string!!")
    if action=="confirm" or action=="rules":
        print("HINT 1:ok so I have chosen",j+"!!!\n and you have",len(x)+2,"chances to guess")
        for i in range(len(x)+1):
            term=x
            query = []
            flag = 0 
            chance=0
            while True:
                query.append(input("Enter the letter: ").lower())
                output = " ".join([x if x in query else "_" for x in term.lower()])
                print(output)
                flag += 1 if query[-1] in term.lower() else 0
                chance+=1
                query = list(set(query))
                if flag == len(set(term)) or chance==len(term)+2:
                    print("YIKES!!you won!!!")
                    print("THANKS FOR PLAYING THE GAME!!HOPE YOU ENJOYED IT!!") 
                    break 
              if flag==len(set(term)) or chance==len(term)+2:
                print("THANKS FOR PLAYING THE GAME!!HOPE YOU ENJOYED IT!!") 
                break
         
elif p=="rules" or store=="rules":
    print("SO THE HANGMAN GAME IS A REALLY SIMPLE GAME\nHere, a random word is picked up from our collection and the player gets limited chances to win the game.")
    print("When a letter in that word is guessed correctly, that letter position in the word is made visible.\nIn this way, all letters of the word are to be guessed before all the chances are over.\nIn other word, I have a secret list of fruits for me,you have to guess the correct fruit")
    print("you shall be getting only 2 more guesses than the total number of alphabets in the string!!")
    new=input("Now let's hope onto the game!!Type CONTINUE to move to the game: ")
    newc=new.upper()
    if newc=="EXIT":
        print("Sorry to see you go!!We shall play next time...")
    elif newc!="CONTINUE" and newc!="EXIT":
        print("OOPS!Wrong command!!Try again pls")
        code=input("Write the correct command: ")
        newcode=code.upper()
    if newc=="CONTINUE" or newcode=="CONTINUE":
        print("HINT 1:ok so I have chosen",j+"!!!and you have",len(x)+2,"chances to guess")
        for i in range(len(x)+1):
            term=x
            query = []
            flag = 0 
            chance=0
            while True:
                query.append(input("Enter the letter: ").lower())
                output = " ".join([x if x in query else "_" for x in term.lower()])
                print(output)
                flag += 1 if query[-1] in term.lower() else 0
                chance+=1
                query = list(set(query))
                if flag == len(set(term)) or chance==len(term)+2:
                    print("YIKES!!you won!!!")  
                    print("THANKS FOR PLAYING THE GAME!!HOPE YOU ENJOYED IT!!") 
                    break 
elif p=="exit" or store=="exit": 
   print("Sorry to see you go!!See ya next time!!")

     
