import random

def ai():
    botchoice = random.randint(1, 3)
    if botchoice == 1:
        return "rock"
    elif botchoice == 2:
        return "paper"
    else:
        return "scissors"

print("Rock/Paper/Scissors")
while True:
    print("Pick:")
    user = input()
    botchoice = ai()
    print("Bot: "+botchoice)
    if user == "exit":
        break
    elif user == "rock":
        if botchoice == user:
            print("Tie")
        elif botchoice == "paper":
            print("You lose")
        else:
            print("You Win")
    elif user == "paper":
        if botchoice == user:
            print("Tie")
        elif botchoice == "scissors":
            print("You lose")
        else:
            print("You Win")
    elif user == "scissors":
        if botchoice == user:
            print("Tie")
        elif botchoice == "rock":
            print("You lose")
        else:
            print("You Win")
    else:
        print("Please enter Rock,paper or scissors")
print(str(5))
print("Thanks for playing")
