import random
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

Scissors='''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player_choice=int(input("Enter your choice 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors': "))
Player_choose=print("You Choose:\n") 
if player_choice==0:
    print(Rock)
elif player_choice==1:
    print(Paper)
else:
    print(Scissors)

computer_choice=random.randint(0,2)
computer_choose=print("Computer choose:\n")

if computer_choice==0:
    print(Rock)
elif computer_choice==1:
    print(Paper)
else:
    print(Scissors)

#combination 1
if player_choice==0 and computer_choice==0:
    print("Draw")
elif player_choice==0 and computer_choice==1:
    print("You lose!")
elif player_choice==0 and computer_choice==2:
    print("You win!")

#combination 2
elif player_choice==1 and computer_choice==0:
    print("You lose")
elif player_choice==1 and computer_choice==1:
    print("Draw")
elif player_choice==1 and computer_choice==2:
    print("You win!")

#combination 3
elif player_choice==2 and computer_choice==0:
    print("You win!")
elif player_choice==2 and computer_choice==1:
    print("You lose")
elif player_choice==2 and computer_choice==2:
    print("Draw")


