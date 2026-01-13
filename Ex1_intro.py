# -------------------------------------------
# Exercise 1: Introduction to Python
# -------------------------------------------
# This exercise introduces you to the basics of text-based programming.
# We will translate what you know from Scratch into Python code!
#
# Key Concepts to practise:
# - Printing to the screen
# - Creating variables
# - Basic math (+, -, *, /)
# - Input from the user
# - Simple IF statements
# -------------------------------------------
# INDIVIDUAL INSTRUCTIONS
# -------------------------------------------
# Work independently. If you get stuck, check your notes or chat with a 
# peer. Use your teacher as a final resort—let's try to problem-solve!
# -------------------------------------------


# -------------------------------------------
# Task 1: Hello World and Variables
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Hello World and Variables\n"
    + "-------------------------------------------")

# TODO:
# 1. Print a message saying "Welcome to Python!"
# 2. Create a variable called 'user_name' and set it to your name.
# 3. Print a message that says "Hello" followed by your variable.
#
# EXAMPLE:
# food = "Pizza"
# print("I love " + food)

# Write your code below:
print("Welcome to Python!")
user_name = 'Sidra Abrahim'
print(f"Hello {user_name}")

# -------------------------------------------
# Task 2: Basic Arithmetic (The Calculator)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Basic Arithmetic\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable called 'num1' and set it to 10.
# 2. Create a variable called 'num2' and set it to 5.
# 3. Create a variable called 'total' that adds num1 and num2 together.
# 4. Print the result.
#
# EXAMPLE:
# apples = 2
# oranges = 4
# fruit_bowl = apples + oranges

# Write your code below:
num1 = 10
num2 = 5
total = num1 + num2
print(f"{num1} + {num2} = {total}")

# -------------------------------------------
# Task 3: User Input and IF Statements
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: User Input and IF Statements\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user "What is the password?" and store it in a variable.
# 2. Use an IF statement to check if the password is "Python123".
# 3. If correct, print "Access Granted".
# 4. Otherwise (ELSE), print "Access Denied".
#
# EXAMPLE:
# colour = input("What is your favourite colour? ")
# if colour == "Red":
#     print("That is a bold colour!")
# else:
#     print("Cool choice.")

# Write your code below:
password = input("what is your password?\n")

if password == "Python123":
    print("Access Granted")
else:
    print("Access Denied")
# -------------------------------------------
# CHECKPOINT & SAVE
# -------------------------------------------
# Run your program. Does it greet you? Does it do the math? 
# Does the password check work?
#
# SAVE TO GIT:
# 1. Save your file.
# 2. In the terminal, type: git add Ex1_intro.py
# 3. Type: git commit -m "Completed tasks"
# 4. Type: git push
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Number Squaring
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 1: Number Squaring\n"
    + "-------------------------------------------")

# TODO: Ask the user for a number, convert it to an integer using int(),
# and print that number multiplied by itself.
#
# EXAMPLE:
# age = int(input("How old are you? "))
# next_year = age + 1

# Write your code below:
num = int(input("Enter a number\n"))
square = num*num
print (square)
# Extension 2: Score Tracker
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Score Tracker\n"
    + "-------------------------------------------")

# TODO: Create a variable 'score' set to 0. 
# Ask the user a simple math question (e.g., 5 + 5). 
# If they get it right, add 10 to the score and print the new total.
#
# EXAMPLE:
# points = 50
# points = points + 5

# Write your code below:
score = 0
answer = int(input("What is 100 * 100?\n"))
if answer == 10000:
    score += 10
    print(f"Well done! Your score is {score}")
else:
    print("You lose!")
# Extension 3: The Length Checker
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: The Length Checker\n"
    + "-------------------------------------------")

# TODO: Ask the user to type a word. 
# Use the len() function to count the letters. 
# If the word is longer than 5 letters, print "That's a long word!"
#
# EXAMPLE:
# animal = "Elephant"
# size = len(animal)

# Write your code below:
word = input("Please Enter a word\n")
length = len(word)

if length > 5:
    print("That's a long word!")
# -------------------------------------------
# SAVE YOUR EXTENSIONS
# -------------------------------------------
# 1. Save your file.
# 2. In the terminal, type: git add Ex1_intro.py
# 3. Type: git commit -m "Completed extensions"
# 4. Type: git push
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The Mini-Bot
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The Mini-Bot\n"
    + "-------------------------------------------")

# TODO:
# Create a small "Chatbot" that:
# 1. Asks the user's name.
# 2. Asks "How are you feeling today?"
# 3. If they say "happy", print "That's great to hear!"
# 4. If they say "sad", print "I'm sorry, I hope your day gets better."
# 5. For any other answer, print "I see, thanks for sharing!"
#
# EXAMPLE:
# if pet == "dog":
#     print("Woof!")
# elif pet == "cat":
#     print("Meow!")
# else:
#     print("What animal is that?")

# Write your code below:
name = input("What is your name? ")
feel = input("How are you feeling today? ")
if feel == "happy":
    print("That's great to hear!")
elif  feel == "sad":
    print("I'm sorry, I hope your day gets better.")
else:
    print("I see, thanks for sharing!")     

# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# Use the terminal to save your final work:
# 1. git add Ex1_intro.py
# 2. git commit -m "Completed advanced activity"
# 3. git push
# -------------------------------------------
