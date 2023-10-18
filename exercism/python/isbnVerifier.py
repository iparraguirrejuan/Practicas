"""
Instructions
The ISBN-10 verification process is used to validate book identification numbers. These normally contain dashes and look like: 3-598-21508-8

ISBN
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

Task
Given a string the program should check if the provided string is a valid ISBN-10. Putting this into place requires some thinking about preprocessing/parsing of the string prior to calculating the check digit for the ISBN.

The program should be able to verify ISBN-10 both with and without separating dashes.

Caveats
Converting from strings to numbers can be tricky in certain languages. Now, it's even trickier since the check digit of an ISBN-10 may be 'X' (representing '10'). For instance 3-598-21507-X is a valid ISBN-10.
"""
def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    checksum = 0
    for i in range(9):
        if isbn[i].isdigit():
            checksum += int(isbn[i]) * (10 - i)
        else:
            return False

    last_character = isbn[9]
    if last_character.isdigit():
        checksum += int(last_character)
    elif last_character.upper() == "X":
        checksum += 10
    else:
        return False

    if checksum % 11 == 0:
        return True
    else:
        return False

   