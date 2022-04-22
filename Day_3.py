#Treasure island Day 3
print('''
888                                                                               
888                                                                               
888                                                                               
888888888d888 .d88b.  8888b. 888  888888d888 .d88b. 88888b.d88b.  8888b. 88888b.  
888   888P"  d8P  Y8b    "88b888  888888P"  d8P  Y8b888 "888 "88b    "88b888 "88b 
888   888    88888888.d888888888  888888    88888888888  888  888.d888888888  888 
Y88b. 888    Y8b.    888  888Y88b 888888    Y8b.    888  888  888888  888888 d88P 
 "Y888888     "Y8888 "Y888888 "Y88888888     "Y8888 888  888  888"Y88888888888P"  
                                                                         888      
                                                                         888      
                                                                         888      
''')

print("Welcome to Treasure Island. Your mission is to find the treasure")
if(input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n") == "left"):
    if(input("You come to a lake. Ther is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n") == "wait"):
        p = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Wich colour do you choose?\n")
        if p == "red":
            print("You get burned by fyre. Game Over")
        elif p == "blue":
            print("You got eaten by beasts. Game Over")
        elif p == "yellow":
            print("You found the treasure. You Win")
        else:
            print("Game Over")
    else:
        print("You get attacked by a trout. Game Over")
else:
    print("You fall into a hole. Game Over")

