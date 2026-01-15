# Strings are immutable sequences of Unicode characters.

# -------------------------------
# 1. CREATING STRINGS
# -------------------------------

# Single quotes
s1 = 'Hello'

# Double quotes
s2 = "World"

# Triple quotes (multiline)
s3 = """This is a
multiline string.""" 
print("Length of s1:", len(s1))  
print("Length of s3:", len(s3))
# Raw strings (ignore escape chars — useful for paths/regex)
path = r"C:\Users\hp\Desktop\python_learning_archive"  

# Using escape characters \ to include quotes or special characters like \, ', ", newline(\n), tab, etc.
print("he said \"Python is easy!\"")  # Represents: "Python is easy!"
print("I am Ali and \nI am \x66rom \"Morocc\157.\"") # \x66 is 'f' and \157 is 'o'
# Empty string
empty = ""

print("Single:", s1)
print("Double:", s2)
print("Multiline:\n", s3)
print("Raw path:", path)

print()

# -------------------------------
# 2. STRING IMMUTABILITY
# -------------------------------
name = "Ali"
# name[0] = "O"  # ❌ Raises TypeError — strings are immutable!

# To "modify", create a new string
new_name = "O" + name[1:]  # "Oli"
print("Original:", name, "| Modified:", new_name)


print()

# -------------------------------
# 3. STRING OPERATORS
# -------------------------------

# Concatenation (+)
greeting = "Hello" + " " + "World"
print("Concatenated:", greeting)

# Repetition (*)
echo = "Hi! " * 3  # "Hi! Hi! Hi! "
print("Repeated:", echo)

# Membership (in / not in)
text = "Python is fun"
print("'Python' in text?", "Python" in text)     # True
print("'Java' in text?", "Java" in text)         # False

print()

# -------------------------------
# 4. STRING INDEXING & SLICING
# -------------------------------
"""
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
 0    1   2   3   4   5  --> Positive indices
-6   -5  -4  -3  -2  -1  --> Negative indices
"""
word = "Python"
# sequence[start:end:step]
print("First char:", word[0])    # 'P'
print("Last char:", word[-1])    # 'n'
print("Slice [1:4]:", word[1:4]) # 'yth'
print("Every 2nd char:", word[::2])  # 'Pto'  # or word[0:-1:2]
print("Reversed:", word[::-1])  # 'nohtyP'


print()
# -------------------------------
# 5. COMMON STRING METHODS
# -------------------------------

text = "  Hello, python!  "

print("Original:", repr(text))                   # repr() shows the string with quotes "  Hello, python!  "
print("Uppercase:", text.upper())                # upper() shows the string in uppercase "  HELLO, PYTHON!  "
print("Lowercase:", text.lower())                # lower() shows the string in lowercase "  hello, python!  "
print("Title Case:", text.title())              # title() capitalizes the first letter of each word "  Hello, Python!  "
print("Stripped:", text.strip())                 # strip() removes leading/trailing whitespace "Hello, python!"
print("Replaced:", text.replace("python", "AI")) # replace() substitutes one substring for another "  Hello, AI!  "
print("Split:", text.split(","))                 # split() splits the string into a list ['  Hello', ' python!  ']

# Find & index
print("Find 'python':", text.find("python"))     # Returns index (9) or -1 if not found
print("Starts with '  H':", text.startswith("  H"))  # True
print("Ends with '!  ':", text.endswith("!  "))      # True

print()

# -------------------------------
# 6. STRING FORMATTING
# -------------------------------

name = "Ali"
age = 22

# f-strings (modern, recommended)
msg1 = f"Hello, I'm {name.upper()} and I'm {age} years old."
print("f-string:", msg1)

# .format() (older but still valid)
msg2 = "Hello, I'm {} and I'm {} years old.".format(name, age)
print(".format():", msg2)

# % formatting (legacy — avoid in new code)
# %d, %c, %s, and %f are some commonly used string formatters.
msg3 = "Hello, I'm %s and I'm %d years old." % (name, age)
print("% formatting:", msg3)

# Formatting numbers
price = 19.99
print(f"Price: ${price:.3f}")  # Price: $19.990

print()

# -------------------------------
# 7. SPECIAL CHARACTERS & ESCAPING
# -------------------------------

# Common escapes
newline = "Line 1\nLine 2"
tabbed = "Col1\tCol2"
quote = "He said, \"Python!\""

print("Newline:\n", newline)
print("Tabbed:", repr(tabbed))
print("Quoted:", quote)

# Use raw strings to avoid escaping
regex_pattern = r"\d{3}-\d{2}-\d{4}"  # SSN pattern
print("Regex (raw):", regex_pattern)

print()

# -------------------------------
# 8. UNICODE & ENCODING
# -------------------------------

# Python 3 strings are Unicode by default
emoji = "Python 🐍 is awesome!"
print("Unicode string:", emoji)

# Encode to bytes (e.g., for file/network I/O)
utf8_bytes = emoji.encode('utf-8')
print("UTF-8 bytes:", utf8_bytes)

# Decode back to string
decoded = utf8_bytes.decode('utf-8')
print("Decoded:", decoded)

print()

# -------------------------------
# 9. COMMON PITFALLS
# -------------------------------

# ❌ Don't use `is` for string equality!
a = "hello"
b = "hello" 
print("a == b:", a == b)     # True 
print("a is b:", a is b)     # Often True (due to interning), but NOT guaranteed! ❌

# ✅ Always use `==` to compare string values.

# Case sensitivity
print("'Hello' == 'hello'?", "Hello" == "hello")  # False

print()




# -------------------------------
# 10. PRACTICE EXAMPLES
# -------------------------------
print("=== PRACTICE EXAMPLES ===") 
# Reverse a string
original = "Python"
reversed_str = original[::-1]
print("Reversed:", reversed_str)  # 'nohtyP'

# Check if palindrome
word = "radar"
is_palindrome = word == word[::-1]
print(f"'{word}' is palindrome?", is_palindrome)  # True

# Join a list into a string
words = ["Python", "is", "great"]
sentence = " ".join(words)
print("Joined:", sentence)  # "Python is great"

print("Length of sentence:", len(sentence))  # 15

# =================================================
# KEY TAKEAWAYS:
# • Strings are immutable
# • Use f-strings for formatting
# • Use ==, not is, for value comparison
# • ' and " are interchangeable — choose to avoid escaping
# • Triple quotes for multiline
# • .strip(), .split(), .join() are essential methods
# • .find() returns -1 if not found; .index() raises an exception
# =================================================