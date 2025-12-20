"""
Comments help programmers understand the code.
Docstrings document modules, functions, classes, and methods.
"""

# -------------------------
# Single-line comments
# -------------------------

# This is a single-line comment
# Comments start with a hash symbol (#)
# They are ignored by the Python interpreter

# Print a message to the screen
print("Hello")


# -------------------------
# Multi-line comments
# -------------------------

# Method 1: Using # on each line
# This is a multi-line comment
# written using hash symbols
# and is meant for programmers only

"""
Method 2: Using triple quotes
This is technically a multi-line string.
If it is NOT assigned to a variable
and NOT placed as a docstring,
it acts like a multi-line comment.
"""

# -------------------------
# Docstrings
# -------------------------

def multiplier(num):
    """
    Function to multiply the value of a number.

    Parameters:
    num (int or float): number to be multiplied

    Returns:
    int or float: multiplied value of num
    """
    return 2 * num


# Accessing the docstring of the function
print(multiplier.__doc__)
# Or
help(multiplier)

# -------------------------
# Key Takeaways
# -------------------------
# - Comments explain the code to programmers
# - Comments are ignored by Python
# - Docstrings document functions, classes, and modules
# - Docstrings are stored in the __doc__ attribute
# - Triple quotes are used for docstrings
