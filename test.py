#! /bin/bash/ env Python3

import random
ls = []

x = random.randint(1,10)
i = input("Enter your name: ")
print(f"The number {x} is assigned to {i}")
ls.append(i)

for l in range(5):
    print(l+1)
print("This is my test code")

for m in range(5):

    user = input("Enter a word: ")
    ls.append(user)

print(ls)
print("Hello world")