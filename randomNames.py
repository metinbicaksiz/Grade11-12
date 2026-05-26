import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images =[rock, paper, scissors]
computerChoice = random.randint(0, len(images)-1)

userChoice = int(input("what do you choose? type 0 for rock, 2 for scissors 3 for paper.\n"))

if userChoice == 0:
    if computerChoice == 0:
        print("It is a draw!")
    elif computerChoice == 1:
        print("You loose!")
    elif computerChoice == 2:
        print("You win!")

if userChoice == 1:
    if computerChoice == 0:
        print("You win!")
    elif computerChoice == 1:
        print("Its a draw")
    elif computerChoice == 2:
        print("You loose!")

    if userChoice == 2:
        if computerChoice == 0:
            print("You loose!")
        elif computerChoice == 0:
            print("You win!")
        elif computerChoice == 2:
            print("It is a draw")
