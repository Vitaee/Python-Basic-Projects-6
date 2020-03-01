import sys
print("Welcome to the Guess My Number App")

a = input("Hello! What is your name: ").title()
print("Well " + a + " I am thinking of a number between 1 and 20")

number = 12 


while number == 12:
    no = int(input("Take a guess: "))

    if no == 11:
	    print("To close!")

    elif no < 10:
	    print("Guess a higher number")

    elif no > 12:
	    print("Guess a lower number")

    elif no == 12:
	    print("You are perfect that was my number")
	    sys.exit()