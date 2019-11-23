#! /bin/bash/ env Python3

import random
ls = []
mercedes = "Estate"
audi = "Avant"
bmw = "Touring"

x = random.randint(1,10)
i = input("Enter your name: ")
print(f"The number {x} is assigned to {i}")
ls.append(i)

for l in range(5):
    print(l+1)
print("This is my test code")
print("PREVIEW")

while True:
    car = input("Enter a car name (Estate, Avant or Touring): ")
    if car.capitalize() == mercedes:
        print("You chose Mercedes")
        break
    elif car.capitalize() == audi:
        print("You chose Audi")
        break
    elif car.capitalize() == bmw:
        print("You chose BMW")
        break
    else:
        print("You must enter Estate, Avant or Touring")


for m in range(5):

    user = input("Enter a word: ")
    ls.append(user)

print(ls)
print("Hello world")
c = 0
while c != 1:
    for i in range(5):
        print("Hello")
    for v in range(3):
        print("THREE")
    input("Press <enter>")
    c = 1