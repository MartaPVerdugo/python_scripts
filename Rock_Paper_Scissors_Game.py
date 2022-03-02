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

#Write your code below this line 👇

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_input >= 3 or user_input < 0:
    print("You typed an invalid number")
elif user_input == 0:
    user_input = rock
elif user_input == 1:
    user_input = paper
elif user_input == 2:
    user_input = scissors
print("You chose: \n")
print(user_input)
computer_input = random.randint(0, 2)

if computer_input == 0:
    computer_input = rock
elif computer_input == 1:
    computer_input = paper
elif computer_input == 2:
    computer_input = scissors
print(f"Computer chose: \n {computer_input}")


if user_input == rock and computer_input == scissors:
    print("You win!")
elif user_input == scissors and computer_input == paper:
    print("You win!")
elif user_input == paper and computer_input == rock:
    print("You win!")
elif computer_input == rock and user_input == scissors:
    print("You lose!")
elif computer_input == scissors and user_input == paper:
    print("You lose!")
elif computer_input == paper and user_input == rock:
    print("You lose!")
elif computer_input == user_input:
    print("It\'s a draw!")
