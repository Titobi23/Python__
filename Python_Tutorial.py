# print ("Hello World")
# This is a comment
# Comments are ignored by the compiler and can be used to make your code more readable


# Variables and Multiple Assignment
# age = 20
# sentence = "my name is avi"

# Sarah, Bob, Mike = 16, 21, 17

# Sarah = Bob = Mike = 17

# name, age = "Titobi", 23



# Arithmetic Operators and Strings
# + - * / % ** //

# age1 = 12
# age2 = 18

# print (age1 + age2) #Addition

# print (age1 - age2) #Subtraction

# print(age1 * age2 ) # Multiplication

# print(age1 / age2) #Division

# print(age1 % age2) #Modulus
# print(age2 % age1) #Modulus

# print(age1 ** age2) #Exponentiation

# print(age1 // age2) #Floor Division


# Strings

# sent1 = "today is a beautiful day"
# print(sent1)

# first_name = "Titobi"
# last_name = "Olatunji"
# print(first_name + " " + last_name)
# print("hi" * 10)

# slicing
# sent = "Titobi was playing basketball"
# print(sent[0:6])   ##indexing starts from zero. so index of T in sent


# Placeholders in Strings   

# name = "Jake"
# print(name + " is 15 years old")

# sentence = "%s is 15 years old"
# print(name + " is 15 years old")

#sentence = "%s %s was the president of the US"
#print(sentence % ("Barack", "Obama"))

# sentence = "%s is %d years old"
# print(sentence % ("Titobi", 23))


# Format Strings
# name = "Titobi"
# print(f"Hello, {name}")

# x = 10
# y = 20
# print(f"The sum of x and y is {x+y}")


# Introduction To Lists
# Ordered items that have an index, and you know the order
# shopping_list = ['apples', 'bananas', 'oranges', 'cheese']
# the list number starts at zero
# print(shopping_list[0])
# print(shopping_list[2])
# print(shopping_list[0:3])
# add items to list
# shopping_list.append('blueberries')
# print(shopping_list[4])
# How to change/update an item in the list
# shopping_list[0] = 'cherries'
# print(shopping_list[0])
# How to delete items in a list
# del shopping_list[1]
# print(shopping_list)
# How to find lengh of list
# print(len(shopping_list))
# How to add lists together
# shopping_list_2 = ['bread', 'jam', 'peanut butter']
# print(shopping_list+shopping_list_2)
# How to multiply lists incaase you want to repeat values multiple times
# print(shopping_list_2 * 2)
# max and min to find the maximum and minimum values in a list
# list_num = [1,4,7,23,6]
# print(max(list_num))
# print(min(list_num))

# Introduction to Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# students = {'bob': 12, 'rachel': 13, 'emily': 15}
# print(students)
# print(students['rachel'])
# How to update the dictionary
# students['rachel'] = 14
# print(students)
# How to delete a key
# del students['emily']
# print(students)
# print(len(students))
# It's crucial for each key to be unique

# Introduction to Tuples
# Tuple is another way of storing collections of data. Unlike lists tuples can't be changed 
# Tuples are immutable - they can't be modified
# tup = ("oranges", "apples", "bananas")
# print(tup)
# Why Use Tuples?
# 1. Consistency
# If we use tuples instead of lists it will make our code more consistent as well as easier to read
# 2. Safety
# We can concatenate tuples to create a new one
# tup2 = (12, 14)
# tup3 = tup + tup2
# print(tup3)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# result = factorial(2)
# print(result)



# Conditional Statements
# Conditions are statements that control whether or not some block of code runs.
# Syntax : condition ? expressionTrue : expressionFalse;
# operates on an if-else principle.
# if 5 > 3:
#     print("Hello")

# if 3 < 2:
#     print("Hello")
# else:
#     print("The condition was not true")
# The indentations are important. The if and else must be on the same line and the print must be on the same line as it shows python what code to execute

# relational operators
# our conditions are built using relational operators
# > < >= <= == !=
# == is used to compare values/variables

# else if statements
# lets us have multiple if statements in the same block
# age = 16
# if age <= 15:
#     print("You are younger than 16")
# elif age == 16:
#     print("You are 16")
# elif age == 17:
#     print("You are 17")
# else:
#     print("You are older than 16")

# We can use multiple operators
# age = 16
# if age < 13:
#     print("You are a child")
# elif age>=13 and age <=18:
#     print("You are a teenager")
# else:
#     print("You are an adult")
# The and operator requires both conditions to be true. Remember logic gates?
# Or needs just one to be true
# if 5 > 3 or 2 < 1:
#     print("Hi")
# logical operators
# and / or


# Introduction to For loops
# what are for loops used for?
# For loops are a powerful tool for iterating over sequences of elements. 
# They can be used to perform a variety of tasks, such as printing the elements of a list, 
# summing the elements of a list, or iterating over the keys and values of a dictionary.
# list1 = ['apples', 'bananas', 'cherries']
# tup1 = (2,6,10)
# Notice the indentation
# for item in list1:
#     print(item)
# for item in tup1:
#     print(item)

# for i in range(0, 11):
#     print(i)
# The range function does not include the end index, just like in slicing and lists. 
# So for numbers 1-10, you need range(0, 11)
# it can also skip numbers
# for i in range(0, 11, 2):
#     print(i)
# The 2 is the increment factor
# For the first 10 multiples of 5
# for i in range(5, 51, 5):
#     print(i)

# Nested for loops? 
# A nested for loop is a loop that is contained within another loop. This allows you to iterate over two or more sets of data simultaneously. For example, you could use a nested for loop to print the numbers from 1 to 10, and then the letters of the alphabet.
# To create a nested for loop, you simply need to write one for loop inside another for loop. The outer for loop will control the number of times the inner for loop is executed. For example, the following code will print the numbers from 1 to 10, and then the letters of the alphabet:
# for i in range(1, 27, 1):
#     for letter in "abcdefghijklmnopqrstuvwxyz":
#         print(i, letter)
# The first for loop will iterate over the numbers from 1 to 10. The second for loop will iterate over the letters of the alphabet. Each time the outer for loop iterates, the inner for loop will be executed once. This will result in the numbers from 1 to 10 being printed, followed by the letters of the alphabet.
# Nested for loops can be used to perform a variety of tasks, such as printing a table of numbers, or iterating over two or more lists of data. They can be a powerful tool for programmers, and can be used to simplify complex code.
# for i in range(0, 5):
#     for j in range(0, 3):
#         print(i * j)
# You can use them in form of ranges


# Introduction to While loops
# while loop will continue running until condition becomes false
# c = 0
# while c < 5:
#     c = c + 1
#     print(c)

# Control Statements
# Control statements are statements that control the flow of execution of a program. They allow you to specify which parts of your program will be executed and in what order.
# Three primary control statements : Break, continue, pass
# break - breaks out of a loop completely and continues with next statement after that. 
# Allows us to terminate a loop prematurely.
# c = 0
# while c < 5:
#     c = c + 1
#     if c == 3:
#         break
#     print(c)
# Continue- allows you to jump back to top of current iteration without executing rest of code block again 
# c = 0
# while c < 5:
#     c = c + 1
#     if c == 3:
#         continue
#     print(c)
# it skips 3 
# Pass- does nothing at all! It's just there as placeholder so we don't get an error when we forget something important
# it's a do nothing command, it serves as a placeholder and alloes you to structure your code 
# even if you haven't decided what should go in a certain block yet.
# c = 0
# while c < 5:
#     c = c + 1
#     if c == 3:
#         pass
#     print(c)


# Try and Except statements
# try is used when we want our program to handle an exceptional situation or error gracefully by
# letting the user know about this problem instead of crashing the whole program.
# Useful in situations when exceptions may be raised
# If the try block encounters any errors in the execution, the control gets passed over to the except block
# try:
#     if name > 3:
#         print("hello")
# except:
#     print("An error was detected")



# Welcome to Functions!
# Functions are crucial in any programing language due to their role in promoting code reuse 
# thereby enhancing the efficiency and compactness of your code.

# Example: A baker makes Titos special bread
# Series of steps: mix, knead, rise, bake
# make_special_bread() performs the function instead of having to write out the steps every time.
# # They are reusable sets of instructions

# def hello_world():
#     print("Hello world!")
# Nothing happens if you run this because we've only defined the function without calling it. 
# Remember! A function needs to be explicitly called to execute its code.

# def greeting(name):
#     print("Hi " + name + "!")

# greeting("Titobi") 

# A function that adds two numbers and gives their sum
# def add(num1, num2):
#     print(num1 + num2)
# add(23, 27)
# Return Statement
# if you want to save the result of the add function instead of printing it. 
# The return statement passes back the result of the computation to wherever the function was called from
# def add(num1, num2):
#     return num1 + num2
# num_sum = add(23,27)
# print(num_sum)

# def mul(num1, num2):
#     return num1 * num2
# print(mul(add(1,2), add(3,4)))
# Functions are reusable codeblocks created with the def keyword


# Built-in Python Functions
# absolute value
# print(abs(-23))

# bool
# checks if a value is true or false depending on the value it holds. False is zero
# print(bool(0))
# print(bool(-1))
# print(bool(2))
# print(bool(3))
# print(bool(4))

# dir
# print(dir("hello"))

#help
# sent = "hello"
# print(help(sent.upper))

#eval
# sent = "print('hi')"
# eval(sent)

# exec - eval, but multiple lines
# Pythons in built tools for converting data types
# str, int, float
# str: Converts its arguement into a string format
# int & float: Used when you have numeric data trapped in string  format
# float: Used when you have a decimal.
# print("hello " + str(100))
# print(123 + int("456"))
# print(float("123.45") + 0.23)

# Define a function called 'calculate_factorial' that takes in one parameter, 'number'. 
# inside the function, write code to calculate the factorial of the given number using loops
# def calculate_factorial(number):
# Calculates the factorial of a given number.
# Args:
# number: The number to calculate the factorial of.

# Returns:
# The factorial of the given number.


#   factorial = 1
#   for i in range(1, number + 1):
#     factorial *= i
#   return factorial



# Object Oriented Programing. 
# OOP - Classes and Objects
# Class: Dog
# Properties: name, age, breed
# Method: bark, eat, sleep, ....

# Object
# Properties: Fido, 5, german shepherd
# Properties: Max, 2, bulldog
# The class is the blueprint/plan, the objects are entitities that generally fall underthe blueprint, 
# but they can have different properties like the german shepherd and bulldog above

# person class
# class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def getName(self):
#        return self.name
    
#    def getAge(self):
#        return self.age
        

#p1 = Person("Bob", 22)
# print(p1.getName())
# print(p1.getAge())


# OOP - Class Inheritance

# Base model - engine, wheels, e.t.c.
# Sports model - powerful engine...
# The variation inherit common features from the base model but also add and modify some features

#class Car:
#    def __init__(self):
#        self.wheels = 4
#        self.seats = 5

#    def drive(self):
#        print("Driving a car....")

# class SportsCar(Car):
#    def __init__(self):
#        # Remember this executes the init function of the parent class
#        super().__init__()
#        self.engine_power = '400 HP'
#        self.seats = 2

#    def drive(self):
#        print("Driving a sports car....")

# Why use this?
#  1. Reusability of code: We dont have to rewrite the attributes for wheels and seats for the sports car
#  2. Easy maintenance and updates: If you want to change a feature for all car types you just need to change \
# it in the car class and the sub classes will inherit it.
#  3. organised structure: It makes our code easier to understand and manage.      

