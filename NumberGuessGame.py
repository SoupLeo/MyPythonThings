import random

def guessinggame(secretnumber):
    for guesstaken in range(1, 4):
     print(str(guesstaken)+".Guess:")
     try:
        guess = int(input())
        if guess < secretnumber:
            print("Too Low")
        elif guess > secretnumber:
            print("Too high")
        else:
            break
     except:
        print("Please input a number")
        guess=0
    if guess == secretnumber:
     print("Congratulations "+name+",the secret number was "+str(secretnumber)+"!")
    else:
      print("Sorry,you lost.The number was: "+str(secretnumber))

leave=False
print("Hello what is your name?")
name = input()
while leave!=True:
 secretnumber = random.randint(8, 10)
 print(name+",im thinking of a number between 1 and 10,can you guess what it is?")
 guessinggame(secretnumber)
 print("Do you wish to leave y/n?")
 exit=input()
 if exit=="y":
     leave=True
print("Thanks for playing my game,goodbye")



