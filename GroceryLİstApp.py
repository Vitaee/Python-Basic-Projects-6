from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m  %H:%M")
print("Welcome to the Grocery List App.")
print("Current Date and Time: ", dt_string)
a = ["Meat","Cheese"]
print("You currently have ", a[0], "and", a[1], "in your list.")

b = input("\nType of food to add to the grocery list: ")
c = input("\nType of food to add to the grocery list: ")
d = input("\nType of food to add to the grocery list: ")

a.append(b.title())
a.append(c.title())
a.append(d.title())

print("\nHere is your grocery list:")
print(a)
print("\nHere is your grocery list sorted:")
print(sorted(a))

print()

print("Simulating grocery shopping..")
print("\nCurrent grocery list:" ,len(a),"items")
print(a)

e = input("What food did you just buy: ").title()
if e in a:
    a.remove(e)
print("Current grocery list:", len(a), "items")
print(a)


g = input("What food did you just buy: ").title()
if g in a:
    a.remove(g)
print("\nCurrent grocery list:" ,len(a),"items")
print(a)

#title() methodu girilen kelime her ne olursa olsun BANANA, aPPLE, vs...
#Onu alıp sadece Banana, Apple , baş harfini büyük yapıyor o kadar.
 

f = input("What food did you just buy: ").title()
if f in a:
    a.remove(f)
print("\nCurrent grocery list:" ,len(a),"items")
print(a)


print("Sorry, the store is out of", a[1])
x = input("What would you like instead: ").title()

print("\nHere is what remains on your grocery list: ")
del a[1]
a.insert(1,x)
print(a)
