# =================================================
# PYTHON USER INPUT — Basics Only (No Conditions, Loops, or Exceptions)
# The input() function always returns a STRING.
# You must convert it to numbers if you want to do math!
# =================================================

# -------------------------------
# 1. GETTING TEXT INPUT
# -------------------------------

# Ask for name and print a greeting
name = input("Enter your name: ") 
print("Hello,", name)

# Ask for favorite color
color = input("What is your favorite color? ")
print("Your favorite color is", color)

# -------------------------------
# 2. GETTING NUMBER INPUT (and converting it)
# -------------------------------

# Ask for age → convert to integer
age_input = input("Enter your age: ")
age = int(age_input)
print("You are", age, "years old")
print("Next year you will be", age + 1)

# Ask for height → convert to float
height_input = input("Enter your height in meters (e.g., 1.75): ")
height = float(height_input)
print("Your height is", height, "meters")

# -------------------------------
# 3. DOING MATH WITH USER INPUT
# -------------------------------

# Get two numbers and add them
num1_input = input("Enter first number: ")
num2_input = input("Enter second number: ")
num1 = float(num1_input)
num2 = float(num2_input)
total = num1 + num2
print("The sum is:", total)

# -------------------------------
# 4. COMBINING TEXT AND INPUT
# -------------------------------

# Build a sentence from user answers
city = input("What city do you live in? ")
hobby = input("What is your hobby? ")
print(name, "lives in", city, "and loves", hobby)

# -------------------------------
# 5. IMPORTANT NOTES (READ THIS!)
# -------------------------------

# 💡 input() ALWAYS gives you a string—even if you type 100!
# 💡 To do math, you must convert:
#       int()   → for whole numbers
#       float() → for decimals
# 💡 Never do:  input() + 5  → this causes an error!
# 💡 Always convert first:  int(input()) + 5

# Example of correct conversion:
number = int(input("Enter a number: "))
double = number * 2
print("Double of your number is:", double)

# -------------------------------
# 6. STRIPPING EXTRA SPACES (OPTIONAL BUT HELPFUL)
# -------------------------------

# .strip() removes spaces at the beginning and end
clean_name = input("Enter your name (spaces will be removed): ").strip()
print("Cleaned name:", clean_name)

# =================================================
# KEY RULES:
# • input() → always returns a string
# • Use int() or float() to convert for numbers
# • Do math only after conversion
# • Use .strip() to clean up accidental spaces
# =================================================