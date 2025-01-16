import string
import random

print("Welcome to Password Generator!")
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

numLetters = int(input("How many letters would you like in your password?"))
numNumbers = int(input("How many numbers would you like in your password?"))
numSymbols = int(input("How many symbols would you like in your password?"))

password = []

for i in range(numLetters):
    randomLetter = random.choice(letters)
    password.append(randomLetter)


for i in range(numNumbers):
    randomNumber = random.choice(numbers)
    password.append(randomNumber)

for i in range(numSymbols):
    randomSymbol = random.choice(symbols)
    password.append(randomSymbol)

random.shuffle(password)
password = "".join(password)
print(password)

