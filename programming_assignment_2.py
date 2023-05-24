print("Hello Python")


#QWrite a Python program to find the area of a triangle?
a = 10
b = 2

## Addition
add = a + b
## Division
div = a/b

print(add)
print(div)

#Q Write a Python program to swap two variables?
var1 = 123
var2 = 111

print('Before swap:\nvar1 = {} and var2 = {}'.format(var1, var2))

temp = var1
var1 = var2
var2 = temp
print('\nAfter swap:\nvar1 = {} and var2 = {}'.format(var1, var2))

#QWrite a Python program to generate a random number?

import random

print(random.random())
print(random.randint(1, 1000))

#Write a Python program to convert kilometers to miles?
km = 6

miles = km/1.60934

print("For {}km equivalent distance in miles = {}".format(km, miles))

#2.Write a Python program to convert Celsius to Fahrenhei?
c = 35

f = (9*c/5)+32

print("For Celsius = {} equivalent Fahrenheit = {}".format(c, f))

#Write a Python program to display calendar?

import calendar
year = 2021
month = 12

print(calendar.month(year, month))

year = 2022

print(calendar.calendar(year))

#Q Write a Python program to solve quadratic equation?

import math

print("ax^2 + bx^1 + c = 0")
print("Enter the coeff a, b and constant c")

a = int(input(("Enter the coeff a: ")))
b = int(input(("Enter the coeff b: ")))
c = int(input(("Enter the constant c: ")))

d = (b**2) - (4*a*c)

root1 = ((-1*b)+(math.sqrt(d))) / (2*a)
root2 = ((-1*b)-(math.sqrt(d))) / (2*a)

print('\nFor quad eq. {}x^2 + ({})x^1 + {}'.format(a,b,c))
print('The solutions are: {} and {}'.format(root1, root2))

#Write a Python program to swap two variables without temp variable?

var1 = 6
var2 = 4

print('Before swap:\nvar1 = {} and var2 = {}'.format(var1, var2))
var2 = var1 + var2
var1 = var2 - var1
var2 = var2 - var1

print('\nAfter swap:\nvar1 = {} and var2 = {}'.format(var1, var2))
