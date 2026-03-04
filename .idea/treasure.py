print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input("You're at a crossroad. Where do you want to go?\n      Type \"left\" or \"right\"").lower()
if crossroad == "right":
    print("you fall into a hole! Game over!")
elif crossroad == "left":
    print("you've come to a lake you need to cross the lake to meet yuvraj dhatt and get your award. The island is in the middle of the lake.")
    waiting = input(" type \"wait\" to wait for a boat. Type \"swim\" to swim across.").lower()
    if waiting == "swim":
        print("you are attacked by a trout. Game over!")
    elif waiting == "wait":
        print("you arrived at the dhatt island unharmed once u open the correct door yuvraj will give you a special surpirise. There is a house with 3 doors.")
        doors = input(" type \"yellow\" to go through the yellow door. type \"blue\" to go through a blue door. Type \"red\" to go through a red door.").lower()
        if doors == "yellow":
            print("you meet yuvraj dhatt well played he will be giving you a massage as your winnning prize")
        elif doors == "red":
            print("you chose the wrong door. Game over!")
        elif doors == "blue":
            print("you chose the wrong door. Game over!")





