#Rock-scissors game Day 4
import random
images = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    ''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''']
humanChoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if humanChoice != '0' and humanChoice != '1' and humanChoice != '2':
    print("Wrong input, you loose")
else:
    humanChoice = int(humanChoice)
    if humanChoice == 0:
        print(images[0])
    elif humanChoice == 1:
        print(images[1])
    else:
        print(images[2])

    computerChoice = random.randint(0,2)
    print("\nComputer Choose:\n")
    if computerChoice == 0:
        print(images[0])
    elif computerChoice == 1:
        print(images[1])
    else:
        print(images[2])
    if humanChoice == computerChoice:
        print("Draw")
    else:
        if humanChoice == 0 and computerChoice == 1:
            print("You Lose")
        elif humanChoice == 0 and computerChoice == 2:
            print("You win")
        elif humanChoice == 1 and computerChoice == 0:
            print("You win")
        elif humanChoice == 1 and computerChoice == 2:
            print("You lose")
        elif humanChoice == 2 and computerChoice == 0:
            print("You lose")
        elif humanChoice == 2 and computerChoice == 1:
            print("You win")
