print("Welcome to Treasure Hunt!")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
userInput = input('Type "left" or "right".\n')

if userInput == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    userInput2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if userInput2 == "wait":
        print("You've arrived at the island unharmed. There is a house with 3 doors.")
        userInput3 = input(" One red, one yellow and one blue. Which colour do you choose?")
        if userInput3 == "red" or userInput3 == "blue":
            print("No treasure.OOPs")
        else:
            print("Yayyy you won!!!")
    else:
        print("You became dinner of sharks oops!")
else:
    print("You fell in a hole lol. Game Over!")