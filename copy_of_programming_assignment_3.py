# -*- coding: utf-8 -*-
"""Copy of Programming Assignment_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oaEFKT3hePd2CAp6KRkMpiH7410imiml

## Programming Assignment_3
----------------

### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
##### Sol.
"""

num = 10

if(num > 0):
    print(num, "is Positive")
elif(num < 0):
    print(num, "is Negative")
else:
    print(num, "is Zero")

num = 0

if(num > 0):
    print(num, "is Positive")
elif(num < 0):
    print(num, "is Negative")
else:
    print(num, "is Zero")

"""### 2. Write a Python Program to Check if a Number is Odd or Even?
##### Sol.
"""

num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(num, "is a Even Nummber")
else:
    print(num, "is an Odd Number")

num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(num, "is a Even Nummber")
else:
    print(num, "is an Odd Number")

"""### 3. Write a Python Program to Check Leap Year?
##### Sol.
"""

year = 2020

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("Leap Year")
else:
    print("Not a Leap Year")

"""### 4. Write a Python Program to Check Prime Number?
##### Sol.
"""

num = int(input("Enter a number: "))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if is_prime(num):
      print(num, "is prime number")
else:
      print(num, "is not prime number")

"""### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
##### Sol.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

lower = 1
upper = 100

print(f"Prime numbers between {lower} and {upper}:")
for num in range(lower, upper + 1):
    if is_prime(num):
        print(num)

num = int(input("Enter a number: "))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if is_prime(num):
      print(num, "is prime number")
else:
      print(num, "is not prime number")

