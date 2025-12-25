# =================================================
# Variables in Python are dynamic; you don't declare types explicitly.
# A variable is a label given to some object.
# The interpreter infers the type based on the assigned value.
# =================================================

# ------------------------------------------
# 1. INTEGER (int) — Whole numbers, positive or negative
a = 2313184475535175361  # Very large integer — valid in Python! (arbitrary precision)
age = 22
population = -500        # negative integers are valid
print("Large integer a:", a)
print("Type of age:", type(age).__name__)
print("Age:", age)

# NUMERIC LITERALS — Integers in different bases
print("\n--- Numeric Literals (Integer Bases) ---")
binary = 0b1010     # Binary → decimal 10
octal = 0o310       # Octal → decimal 200
decimal = 100       # Decimal
hexadecimal = 0x12c # Hexadecimal → decimal 300

print("Binary 0b1010 =", binary)
print("Octal 0o310 =", octal)
print("Decimal 100 =", decimal)
print("Hex 0x12c =", hexadecimal)

# ------------------------------------------
# 2. FLOAT — Decimal numbers (double precision by default)
price = 19.99
temperature = -3.5
print("\nType of price:", type(price).__name__)
print("Price:", price)

# Float literals
float_1 = 10.5
float_2 = 1.5e2  # Scientific notation = 150.0

# Demonstrate floating-point precision limitation
print("\nFloating-point precision demo:")
print("0.1 in memory:", format(0.1, '.50f'))

print("Float 10.5 =", float_1)
print("Float 1.5e2 =", float_2)

# ------------------------------------------
# 3. BOOLEAN (bool) — Only True or False (capitalized!)
is_student = True
is_adult = age >= 18
print("\nType of is_student:", type(is_student).__name__)
print("Is adult?", is_adult)

# ------------------------------------------
# 4. STRING (str) — Flexible quoting: 'single', "double", or triple quotes
name = 'Ali'
greeting = "Hello, world!"
sentence = 'He said, "Python is easy!"'   # Mix quotes without escaping
quote = "She replied, 'Indeed!'"          # Vice versa

# Multiline strings
bio = """Name: Ali
Age: 22
Loves: AI, Linux, and open-source"""

print("\nType of name:", type(name).__name__)
print("Name:", name)
print("Greeting:", greeting)
print("Multiline bio:\n", bio)

# f-strings (modern, efficient, readable)
num_bananas = 10
bananas = f"You have {num_bananas} bananas"
print(bananas)
print(f"my name is {name}, I'm {age} years old.")
print(f"Bio:\n{bio}")  # f-strings work with multiline strings

# String concatenation (less preferred)
first_name = "Ali"
last_name = " Belyoum"  # Note: space included here
full_name = first_name + last_name
print("Full name via +:", full_name)

# ⚠️ Reminder: f-strings are safer and more readable!
print(f"Full name via f-string: {first_name}{last_name}")

# ------------------------------------------
# 5. COMPLEX — Built-in support for complex numbers!
signal = 3 + 4j
print("\nType of signal:", type(signal).__name__)
print("Complex number:", signal)
print("Real part:", signal.real, "| Imaginary part:", signal.imag)

# ------------------------------------------
# 6. NONE — Represents absence of a value (not zero, False, or "")
result = None
print("\nType of result:", type(result).__name__)
print("Result =", result)

# None vs. string "None"
my_none = None
print("my_none is None?", my_none is None, "| Type:", type(my_none).__name__)

my_none = "None"  # Now it's a string!
print('my_none = "None" → Value:', my_none, "| Type:", type(my_none).__name__)

# =================================================
# CONSTANTS (by convention: UPPER_SNAKE_CASE)
# Python has no 'const' — this is a human-readable convention only.
# =================================================
PI = 3.14159
MAX_USERS = 1000
API_URL = "https://api.example.com"

print("\n--- Constants (convention only) ---")
print("PI ≈", PI)
print("Max users allowed:", MAX_USERS)

# =================================================
# DYNAMIC TYPING DEMO
# A variable can change type at any time!
# =================================================
x = 10
print("\nDynamic typing demo:")
print("x =", x, " | Type:", type(x).__name__)

x = "Now I'm a string!"
print("x =", x, " | Type:", type(x).__name__)

x = True
print("x =", x, " | Type:", type(x).__name__)

# =================================================
# MULTIPLE ASSIGNMENT — Save space and improve readability
# =================================================

# Assign different values to multiple variables
a, b, c = 1, 2.5, "Hello"
print("\nMultiple assignment (different values):")
print("a =", a, " | Type:", type(a).__name__)
print("b =", b, " | Type:", type(b).__name__)
print("c =", c, " | Type:", type(c).__name__)

# Assign same value to multiple variables
n = m = p = 5
print("\nMultiple assignment (same value):")
print("n =", n, "\nm =", m, "\np =", p)
