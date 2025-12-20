# Python Indentation and Coding Style

## Python Syntax vs Other Languages
- Python is designed for **readability**, close to English with mathematical influence
- Instructions end with **new lines**, not semicolons or parentheses
- **Indentation defines scope** of loops, functions, and classes
- Other languages rely on `{}` to define blocks, Python does not

Key idea  
In Python, indentation is **syntax**, not style

---

## What is Indentation
Indentation is the **leading whitespace** before a statement  
It can be spaces or tabs, but spaces are strongly preferred

---

## Why Indentation Matters
- Improves code readability
- Defines **blocks of code**
- Replaces curly braces used in C, C++, Java

Used for:
- if / else
- for / while
- functions
- classes

---

## How Indentation Works
- Same indentation level means same block
- Block starts after `:`
- Block ends when indentation decreases
- Wrong indentation makes code invalid or logically wrong

Example:
```python
if x > 0:
    print("Positive")
print("Done")
