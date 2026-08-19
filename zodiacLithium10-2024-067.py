# Peralta, Raillyq Lairdswill S.
# 9-Lithium

# ZODIAC SIGN CALCULATOR
def getZodiacSign(birthyear):
    # INPUT VALIDATION
    if birthyear < 1900:
        # RESULT
        return "Invalid year. Please enter a year greater than or equal to 1900."
    else:
        # ZODIAC SIGN DEFINITION
        zodiac_signs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
                        "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
        # CALCULATION
        index = (birthyear - 1900) % 12
        # RESULT
        return f"Your Chinese Zodiac sign is {zodiac_signs[index]}."

# MAIN FUNCTION
def main():
    # USER INPUT
    try:
        birthyear = int(input("Enter your birth year: "))
        result = getZodiacSign(birthyear)
        print(result)
    # INPUT VALIDATION
    except ValueError:
        print("Please enter a valid integer for the birth year.")

# CODE EXECUTION
if __name__ == "__main__":
    main()
