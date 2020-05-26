import random

rand = random.randint(1, 99)

print("This is an interactive guessing game!\nYou have ", end='')
print("to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.\nGood luck!\n")

cpt = 0
nb = 0
while (int(nb) != rand):
    print("What's your guess between 1 and 99?")
    nb = input(">> ")
    cpt += 1
    if nb == "exit":
        print("Goodbye!")
        exit(0)
    if not nb.isdigit():
        print("Thats not a number")
        nb = 0
    else:
        if int(nb) < rand:
            print("Too low!")
        elif int(nb) > rand:
            print("Too high!")
        elif int(nb) == 42:
            print("The answer to the ultimate question of life,", end='')
            print("the universe and everying is 42")
            if cpt == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in", cpt, "attempts")
        else:
            if cpt == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in", cpt, "attempts")
