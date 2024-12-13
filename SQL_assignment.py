# Activity 1
# Problem Statement:
# Write a code in python in which you can get “Fizz Buzz” for all numbers which can be divided by (3, 5, 15). The range should from (1 to 100).

# Questions:
# - Which operator you will use in order to execute this code?

for num in range (1,101):
    if num%3 ==0 and num%5 ==0 and num%15 ==0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    elif num%15 ==0:
        print('all')
    
    else:
        print(num)

# The operator used in this code is module operator (%) to check the divisibility, AND used to combined the condition in 'if loop condition'

# Activity 2
# Problem Statement:
# How to swap all uppercase characters to lowercase and vice versa?

# Questions:
# - How the user will enter the character?
# - How it will swap?
# - Which commands will be used to convert each other?

"""
How to enter the character:
Write the text e.g
Details = My name is Iyanu

How it will swap:
Upper case will change to lower case and vice versa using the command .swapcase()

Commands to be used:
.swapcase
"""
Details = 'My name is Iyanu'
print(Details.swapcase())

# Activity 3
# Problem Statement:
# Swap the numbers with and without the 3rd Variable.

# Questions:
# - How you will create and store the value in 3rd variable?
# - How you will do it without the 3rd Variable?
"""
How to create and store value in 3rd variable:
Firstly create variables
e.g a = 6
    b = 9
Then create temporary variable to hold one of the variable
g = a (the value of 'a' will move to 'g')

How to do it without 3rd variable:
To store the value without variable we can use arithmetic method
e.g
    a = a + b
    b = a - b
    a = a - b
    print(a)
USING XOR (^)
e.g
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a,b)

"""
a = 6
b = 9
g = a
print(g)

a = a + b
b = a - b
a = a - b
print(a,b)

a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

# Activity 4
# Problem Statement:
# Write a code in python which will give you a Fibonacci series to a number when you enter it.

# Questions:
# - How you will you deal when a user inputs ‘0’?
# - How the user will deal when a user inputs ‘1’?
# - Which loops and statements do you use for the iterations?


def fibonacci(n):
    # Handle invalid input
    if n < 0:
        raise ValueError("Please enter a positive number.")
    # Special cases for 0 and 1
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    # Generate Fibonacci series up to n
    a, b = 0, 1
    result = []  # List to store Fibonacci numbers
    while a <= n:
        result.append(a)
        a, b = b, a + b
    return result  

try:
    num = int(input("Enter a positive integer to generate the Fibonacci series: "))
    output = fibonacci(num)
    print("Fibonacci series:", output)
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# When user input '0': the series will return "0"
# When user input '': the series will return "0,1" which are the first two elements of the series
# While loop is used to calculate the fibonacci series, if and elif statements used for conditional statement

# Activity 5
"""
Problem Statement:
Create a game in which user guesses a random number in python.

Questions:
- How will generate random number and how will you set the range?
- How to add attempts in your code, that user can have only 5 attempts to play?
- How will you subtract a attempt when user plays it one time?
- How will you show the ‘YOU WON!’ and ‘YOU LOST’ message?
"""
import random
def guess_game():
    #generate random number
    guess_num = random.randint(1,20)
    # add an attempts number
    attempts = 5
    print('Welcome to randon guessing game%')
    print('Instruction: guess the number between 1 and 20 and win the prize. You have 5 attempts')
    while attempts > 0:
        try:
            your_num = int(input(f"Enter your guess number ({attempts} attempts left): "))
            if your_num == guess_num:
                print('Congrat! you have won: ')
                return
            elif your_num > guess_num:
                print("Try again the number is too high: ")
            elif your_num < guess_num:
                print("Try again the number is too low: ")
            attempts -= 1
        except ValueError: 
            print ('please enter the positive integer number: ')
    print(f'oh, sorry, you have lost, the correct number is {guess_num}. ')
guess_game()

# Activity 6
# Problem Statement:
# Create a Basic Calculator that can do Addition, Subtraction, Multiplication and Division in Python.

# Questions:
# - How to create Choices for the user?
# - How the user input two numbers?
# - How can you add your define functions inside your If-else statements?
# - How do stop the calculations at a certain part?
# - How do you cope with this when a user will type a invalid input?

# Define functions for basic operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

# Calculator
def calculator():
    while True:
        # Display options to the user
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("0. Exit")
        
        try:
            # Get user's choice
            choice = int(input("Enter your choice (0-4): "))
            
            if choice == 0:
                print("Exiting the calculator. Goodbye!")
                break  # Exit the loop
            
            # Ensure valid choice
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice! Please select a number between 0 and 4.")
                continue
            
            # Get two numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the chosen operation
            if choice == 1:
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == 2:
                print(f"The result of subtraction is: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"The result of multiplication is: {multiply(num1, num2)}")
            elif choice == 4:
                print(f"The result of division is: {divide(num1, num2)}")
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")

calculator()
