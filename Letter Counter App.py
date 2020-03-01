print("Welcome to the letter counter app")
print()

a = input("What is your name: ")
print("Hello " + a)
print("I will count the number of time that specific letter occurs in a message")
print()

b = input("Please enter a message: ")
c = input("Which letter would you like to count the occurrences of: ")

d = b.count(c)
print(a, "your message has", d, c,"'s in it")
