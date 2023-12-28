print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to Treasure Game!\nYour mission is to find the treasure")
first_choice = input("What would you like to go ('left' or 'right')")
if first_choice == "left":
    print("There was a well on the left and you fell into it, Game Over!")
elif first_choice == "right":
    second_choice = input("there is beach on the right and you should chose that you want to 'wait' or 'swim': ")
    if second_choice == "wait":
        third_choice = input(
            "right choice, now a boat take care of you but there are three doors, which one do you pick?"
            " 'red' or 'yellow' or 'blue' : ")
        if third_choice == "red":
            print("You picked the right one, the treasure is there, YOU WINE")
        elif third_choice == "yellow":
            print("You picked the wrong, Game Over!")
        elif third_choice == "blue":
            print("You picked the wrong, Game Over!")
        else:
            print("You picked the wrong, Game Over!")
    elif second_choice == "swim":
        print("sorry, Whales eat you, Game Over!")
    else:
        print("Sorry, I didn't understand, so Game Over!")
else:
    print("Sorry, I didn't understand, so Game Over!")
