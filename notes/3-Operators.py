# ======= ARITHMETIC OPERATORS ========
#    ** --> Exponent
#    %  --> Modulus/Remainder
#    // --> Integer (floor) Division
#    /  --> True Division (always float)
#    *  --> Multiplication
#    -  --> Subtraction
#    +  --> Addition
# ==========================================

print("=== Arithmetic Operators ===")
print(2 ** 3)        # 8
print(10 % 3)        # 1
print(10 // 3)       # 3 (floor division)
print(10 / 3)        # 3.3333333333333335
print(2 * 3)         # 6
print(5 - 2)         # 3
print(2 + 3)         # 5
print(0xFB + 0b10)   # Hex (251) + Binary (2) = 253

# Operator Precedence: 
# 1. () → 2. ** → 3. *, /, //, % (left-to-right) → 4. +, - (left-to-right)
result = 2 + 3 * 4 ** 2 / (1 + 1)
print("2 + 3 * 4**2 / (1+1) =", result)  # 26.0

# Left-to-right for same precedence
print("8 / 4 * 2 =", 8 / 4 * 2)   # 4.0 → (8/4)*2
print("10 - 3 + 2 =", 10 - 3 + 2) # 9   → (10-3)+2

print()

# ======= RELATIONAL OPERATORS (return bool) ========
#    == --> Equal
#    != --> Not equal
#    <  --> Less than
#    >  --> Greater than
#    <= --> Less than or equal
#    >= --> Greater than or equal
# ==========================================

print("=== Relational Operators ===")
x, y = 10, 12
print('x > y is', x > y)   # False
print('x < y is', x < y)   # True
print('x == y is', x == y) # False
print('x != y is', x != y) # True
print('x >= y is', x >= y) # False
print('x <= y is', x <= y) # True

print()

# ======= LOGICAL OPERATORS (for bools) ========
#    and --> AND (short-circuits)
#    or  --> OR  (short-circuits)
#    not --> NOT
# ==========================================

print("=== Logical Operators ===")
a, b = True, False
print('a and b is', a and b)  # False
print('a or b is', a or b)    # True
print('not a is', not a)      # False

print()

# ======= BITWISE OPERATORS (on integer bits) ========
#    &  --> AND
#    |  --> OR
#    ^  --> XOR (exclusive OR)
#    ~  --> NOT (two's complement: ~n = -(n+1))
#    << --> Left shift  (x << n == x * 2**n)
#    >> --> Right shift (x >> n == x // 2**n for x >= 0)
# ==========================================

print("=== Bitwise Operators ===")
x = 5  # Binary: 0101
y = 3  # Binary: 0011

print('x & y is', x & y)   # 1  → 0001
print('x | y is', x | y)   # 7  → 0111
print('x ^ y is', x ^ y)   # 6  → 0110
print('~x is', ~x)         # -6 → because ~n = -(n + 1)
print('x << 1 is', x << 1) # 10 → 5 * 2^1
print('x >> 1 is', x >> 1) # 2  → 5 // 2^1

print()
# =================================================
# MEMBERSHIP OPERATORS: in, not in
# IDENTITY OPERATORS: is, is not
# =================================================

# Membership: check if a value exists in a sequence (str, list, dict keys, etc.)
x = 'Hello world'
y = {1: 'a', 2: 'b'}

print("'H' in x:", 'H' in x)               # True → 'H' is in the string
print("'hello' not in x:", 'hello' not in x)  # True → case-sensitive!
print("1 in y:", 1 in y)                   # True → checks KEYS of dict
print("'a' in y:", 'a' in y)               # False → 'a' is a VALUE, not a key

print()

# Identity: check if two variables refer to the SAME object in memory
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

# Small integers (-5 to 256) are cached → same object
print("x1 is y1:", x1 is y1)               # True
print("x1 is not y1:", x1 is not y1)       # False

# String literals are often reused in CPython, but this is an implementation detail
print("x2 is y2:", x2 is y2)               # Usually True, but not guaranteed by the language

# Lists are mutable → new objects even if content is same
print("x3 is y3:", x3 is y3)               # False
print("x3 == y3:", x3 == y3)               # True → values equal, but different objects

print()
# 💡 Key Insight:
# - Use == to compare VALUES
# - Use is to compare IDENTITY (same object in memory)
# - For numbers/strings, prefer == unless you specifically need object identity (e.g., `if x is None`)