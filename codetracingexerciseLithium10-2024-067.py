# Peralta, Raillyq Lairdswill S.
# 9-Lithium

# CODE #1:
"""
a) If the name is “Joseph The Dreamer” and the numeric number is 5, the output will be:
   "J
    o
    s
    e
    p"
    because the function greet_students() takes the name and nChar as arguments.
    Then it iterates through the range of nChar (which is 5 in this case) and prints each character of the name on a separate line at the corresponding index.
b) Using 20 for the numeric number will result in an IndexError because the name "Joseph The Dreamer" has only 18 characters (including spaces).
   When the function tries to access the character at index 19, it will be out of range, which will cause an error.
c) To fix the error, you can add an input validator to make sure that nChar does not exceed the length of the name. Like this:"""

# GREETING FUNCTION
def greet_students(name, nChar):
    # INPUT VALIDATION
    if nChar > len(name):
        print("The numeric number exceeds the length of the name. Please enter a valid number.")
    # PER CHARACTERPRINTING
    else:
        for i in range(nChar):
            print(name[i])

# INPUT AND OUTPUT
name = input("Enter a name: ")
nChar = int(input("Enter any numeric number: "))
greet_students(name, nChar)

# CODE #2:
"""
a) The syntax error was that the print statement used 0 instead of the variable i in the loop.
   This is the corrected code:
"""

# GREETING FUNCTION
def greet_students(name, nChar):
    # TRIANGLE PRINTING
    for i in range(nChar):
        print(name[i : nChar])

# INPUT AND OUTPUT
name = input("Enter a name: ")
greet_students(name, len(name))

# CODE #3:
# CALCULATION
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

# INPUT AND OUTPUT
n = 0
while n < 1 or n > 100:
    n = int(input("Enter a number between 1 and 100: "))
print(f"Sum of all squared numbers until {n} is {sum_of_squares(n)}.")                   