# import random
# print(random.randint(1,10))  # Output: Random integer between 1 and 10
# print(random.random()) # Returns a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive).
# print(random.uniform(5.5, 10.5))  # Output: Random float between 5.5 and 10.5
#
# colors = ['red', 'blue', 'green']
# print(random.choice(colors))  # Output: Randomly selected color, returns the element
# print(random.choices(colors, weights=[10, 1, 1], k=2))  # Output: Biased selection returns a list
# print(random.sample(colors, 2))  # Output: 2 unique random colors and returns a list
#
# deck = [1,2,3,4,5,6,7,8,9]
# random.shuffle(deck)
# print(deck)
#

import random

userChoice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
print("You Chose:")

if userChoice == "0":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif userChoice == "1":
    # Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

choice = ['0', '1', '2']
computerChoice = random.choice(choice)

print("Computer Chose: ")
if computerChoice == "0":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

if computerChoice == "1":
    # Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

if computerChoice == "2":
    # Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if userChoice == computerChoice:
    print("That's a draw")
elif userChoice == '0' and computerChoice == '1':
    print("You Lose!")
elif userChoice == '0' and computerChoice == '2':
    print("You win!")
else:
    print("You Lose!")




