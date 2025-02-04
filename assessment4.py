def check_triangle_validity(angle1, angle2, angle3):
    """
    Check Triangle Validity
    Asks the user for three angles of a triangle and checks if they form a valid triangle.
    """
    if angle1 + angle2 + angle3 == 180:
        return "This is a valid triangle."
    else:
        return "This is not a valid triangle."


def check_prime_number(number):
    """
    Check Number is Prime or Not (Basic Check)
    Asks the user for a number and checks if it is prime.
    """
    if number <= 1:
        return f"{number} is not a prime number."
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number."
    return f"{number} is a prime number."


def find_largest_of_four_numbers(num1, num2, num3, num4):
    """
    Find the Largest of Four Numbers
    Asks the user for four numbers and prints the largest among them.
    """
    return max(num1, num2, num3, num4)


def calculate_electricity_bill(units):
    """
    Electricity Bill Calculator
    Asks the user for units consumed and calculates the electricity bill.
    """
    if units <= 100:
        bill = units * 5
    else:
        bill = 100 * 5 + (units - 100) * 8
    return f"Your electricity bill is ₹{bill}"


def check_blood_donation_eligibility(age, weight):
    """
    Check Whether a Person Can Donate Blood
    Asks the user for their age and weight.
    """
    if age >= 18 and weight >= 50:
        return "You are eligible to donate blood."
    else:
        return "You are not eligible to donate blood."


def calculate_discount(bill_amount):
    """
    Calculate Discount on Shopping
    Asks the user for the total bill amount.
    """
    if bill_amount >= 5000:
        discount = 0.20 * bill_amount
        final_bill = bill_amount - discount
        return f"You get a 20% discount! Pay ₹{final_bill}"
    else:
        discount = 0.10 * bill_amount
        final_bill = bill_amount - discount
        return f"You get a 10% discount! Pay ₹{final_bill}"


def determine_triangle_type(side1, side2, side3):
    """
    Determine Type of Triangle
    Asks the user for three sides of a triangle and determines the type.
    """
    if side1 == side2 == side3:
        return "It is an equilateral triangle."
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "It is an isosceles triangle."
    else:
        return "It is a scalene triangle."


def check_atm_withdrawal(account_balance, withdrawal_amount):
    """
    ATM Withdrawal Check
    Asks the user for account balance and withdrawal amount.
    """
    if withdrawal_amount <= account_balance:
        return "Withdrawal successful."
    else:
        return "Insufficient balance"


def convert_temperature(conversion_type, temperature):
    """
    Convert Temperature (Celsius to Fahrenheit or Vice Versa)
    Asks the user if they want to convert Celsius to Fahrenheit or vice versa.
    """
    if conversion_type == 1:
        fahrenheit = (temperature * 9 / 5) + 32
        return f"Temperature in Fahrenheit: {fahrenheit:.2f}°F"
    elif conversion_type == 2:  # Fahrenheit to Celsius
        celsius = (temperature - 32) * 5 / 9
        return f"Temperature in Celsius: {celsius:.2f}°C"
    else:
        return "Invalid conversion type."


def check_multiple(num1, num2):
    """
    Check If a Number is a Multiple of Another
    Asks the user for two numbers and checks if the first number is a multiple of the second.
    """
    if num1 % num2 == 0:
        return f"{num1} is a multiple of {num2}."
    else:
        return f"{num1} is not a multiple of {num2}."


print(
    convert_temperature(int(input("Enter a number:")), int(input("Enter temperature")))
)
