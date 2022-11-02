import random

random.seed()

namenumlist = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
nametypelist = ["of Spades.", "of Hearts.", "of Clovers.", "of Diamonds."]
cardlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
aces = ["A", "A"]
deck = [[0] * 13] * 4
status = True
decision = 0
val = 0
starter = True
condv = val != 1 and val != 11

for i in range(5):
    if i < 4:
        for k in range(13):
            deck[i][k] = cardlist[k]
    elif i >= 4:
        for k in range(2):
            deck[i][k] = aces[k]
    if i == 3:
        deck.append(aces)

a = random.randint(0, 4)
if a != 4:
    b = random.randint(0, 12)
else:
    b = random.randint(0, 1)
player = deck[a][b]
condp = player != 1 and player != 11

if a != 4:
    print("Player has drawn", namenumlist[b], nametypelist[a])
else:
    print("Player has drawn an Ace.")


if player == "J" or player == "Q" or player == "K":
    player = int(10)
elif player == "A":
    while condp:
        player = int(input("Ace! What value do you prefer, 1 or 11? "))
        if player != 1 and player != 11:
            print("You have to choose either 1 or 11.")


while status == True:
    print("Your sum is",player,", keep going? ", end="")
    decision = input("")
    if decision == "Yes" or decision == "yes" or decision == "y" or decision == "Y":
        a = random.randint(0, 4)
        if a != 4:
            b = random.randint(0, 12)
        else:
            b = random.randint(0, 1)
        val = deck[a][b]
        if val == "J" or val == "Q" or val == "K":
            val = int(10)
        elif val == "A":
            while condv:
                val = int(input("Ace! What value do you prefer, 1 or 11? "))
                if val != 1 and val != 11:
                    print("You have to choose either 1 or 11.")
        player += val
        if a != 4:
            print("Player has drawn", namenumlist[b], nametypelist[a])
        else:
            print("Player has drawn an Ace.")
        if player > 21:
            print("Crashed! You exceeded 21.")
            print("Computer won!")
            starter = False
            break
        print("Current sum = ", player)
    else:
        print("Ended at", player)
        break

if starter == True:
    a = random.randint(0, 4)
    if a != 4:
        b = random.randint(0, 12)
    else:
        b = random.randint(0, 1)
    computer = deck[a][b]
    if a != 4:
        print("Computer has drawn", namenumlist[b], nametypelist[a])
    else:
        print("Computer has drawn an Ace.")
    choice = [0, 1]
    acechoice = [1, 11]

    if computer == "J" or computer == "Q" or computer == "K":
        computer = int(10)
    elif computer == "A":
        computer = int(random.choice(acechoice))

    while status == True:
        print("Computer sum is", computer)
        if computer <= player:
            decision = 1
        if decision == 1:
            a = random.randint(0, 4)
            if a != 4:
                b = random.randint(0, 12)
            else:
                b = random.randint(0, 1)
            val = deck[a][b]
            if val == "J" or val == "Q" or val == "K":
                val = int(10)
            elif val == "A":
                val = int(random.choice(acechoice))
            computer += val
            if a != 4:
                print("Computer has drawn", namenumlist[b], nametypelist[a])
            else:
                print("Computer has drawn an Ace.")
            if computer > 21:
                print("Crashed! Computer's sum was", computer,"and exceeded 21.")
                break
            if computer > player:
                print("Computer won! Computer's sum was", computer)
                break
            print("Computer's sum = ", computer)
        else:
            print("Computer ended at", computer)
            break
