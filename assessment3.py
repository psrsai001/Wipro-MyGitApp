def check_even_odd(number):
    """
    Check Even or Odd
    Asks the user for a number and prints whether it is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."


def check_positive_negative_zero(number):
    """
    Check Positive, Negative, or Zero
    Asks the user for a number and determines if it's positive, negative, or zero.
    """
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."


def find_greater_number(num1, num2):
    """
    Find the Greater Number
    Asks the user for two numbers and prints the greater one.
    """
    if num1 > num2:
        return f"{num1} is greater."
    else:
        return f"{num2} is greater."


def check_driving_license_eligibility(age):
    """
    Age Check for Driving License
    Asks the user for their age and checks if they are eligible for a driving license (age ≥18).
    """
    if age >= 18:
        return "You are eligible for a driving license."
    else:
        return "You are not eligible for a driving license."


def check_leap_year(year):
    """
    Check Leap Year
    Asks the user for a year and checks if it's a leap year.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."


def check_vowel_or_consonant(letter):
    """
    Check Vowel or Consonant
    Asks the user for a single letter and determines if it's a vowel (a, e, i, o, u) or consonant.
    """
    letter = letter.lower()
    if letter in "aeiou":
        return f"{letter} is a vowel."
    else:
        return f"{letter} is a consonant."


def find_largest_among_three_numbers(num1, num2, num3):
    """
    Find Largest Among Three Numbers
    Asks the user for three numbers and prints the largest among them.
    """
    if num1 >= num2 and num1 >= num3:
        return f"{num1} is the largest."
    elif num2 >= num1 and num2 >= num3:
        return f"{num2} is the largest."
    else:
        return f"{num3} is the largest."


def check_divisibility_by_5_and_11(number):
    """
    Check Divisibility by 5 and 11
    Asks the user for a number and checks if it is divisible by both 5 and 11.
    """
    if number % 5 == 0 and number % 11 == 0:
        return f"{number} is divisible by both 5 and 11."
    else:
        return f"{number} is not divisible by both 5 and 11."


def check_uppercase_or_lowercase(letter):
    """
    Check for Uppercase or Lowercase Letter
    Asks the user for a single letter and determines if it's uppercase or lowercase.
    """
    if letter.isupper():
        return f"{letter} is an uppercase letter."
    elif letter.islower():
        return f"{letter} is a lowercase letter."
    else:
        return "Not a valid alphabet"


def check_pass_or_fail(marks):
    """
    Pass or Fail (Grading System)
    Asks the user for their marks (out of 100). If the marks are ≥40, print "Pass", otherwise print "Fail".
    """
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
