print("Welcome to Tip Calculator!")

total_bill = float(input("What is your total bill? $"))
tip = int(input("How much tip would you like to give? 10, 20, or 15%?"))
people = int(input("How many people to split the bill? "))

split = total_bill + (total_bill * tip / 100)
split2 = split / people

print(f"Each person should pay: {split2:.2f}")

