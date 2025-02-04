def print_first_n_odd_numbers(n):
    """
    Print First N Odd Numbers (Skip Even Numbers Using Continue)
    Asks the user for a number N and prints the first N odd numbers using continue.
    """
    count = 0
    num = 1
    output = ""
    while count < n:
        if num % 2 == 0:
            num += 1
            continue  # Skip even numbers
        output += str(num) + " "
        num += 1
        count += 1
    return output.strip()


def find_first_multiple_of_7(n):
    """
    Find First Multiple of 7 Using Break
    Asks the user for a number N and finds the first number greater than N that is a multiple of 7 using break.
    """
    num = n + 1
    while True:
        if num % 7 == 0:
            break
        num += 1
    return f"First multiple of 7 after {n} is {num}"


def check_if_prime(x):
    """
    Check if a Number is Prime
    Asks the user for a number X and checks if it's prime using a loop.
    """
    if x <= 1:
        return f"{x} is not a prime number."

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return f"{x} is not a prime number."
    return f"{x} is a prime number."


def find_largest_digit(number):
    """
    Find the Largest Digit in a Number
    Asks the user for a number and finds the largest digit.
    """
    largest_digit = 0
    number = abs(number)
    while number > 0:
        digit = number % 10
        if digit > largest_digit:
            largest_digit = digit
        number //= 10
    return f"Largest digit: {largest_digit}"


def find_smallest_digit(number):
    """
    Find the Smallest Digit in a Number
    Asks the user for a number and finds the smallest digit.
    """
    smallest_digit = 9  # Initialize with the largest possible digit
    number = abs(number)
    while number > 0:
        digit = number % 10
        if digit < smallest_digit:
            smallest_digit = digit
        number //= 10
    return f"Smallest digit: {smallest_digit}"


def find_lcm(num1, num2):
    """
    Find LCM (Least Common Multiple) of Two Numbers
    Asks the user for two numbers and finds their LCM using a loop.
    """
    max_num = max(num1, num2)
    lcm = max_num
    while True:
        if lcm % num1 == 0 and lcm % num2 == 0:
            break
        lcm += max_num
    return f"LCM of {num1} and {num2} is {lcm}"


def find_gcd(num1, num2):
    """
    Find GCD (Greatest Common Divisor) of Two Numbers
    Asks the user for two numbers and finds their GCD using a loop.
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return f"GCD of {num1} and {num2} is {num1}"


def find_first_n_armstrong_numbers(n):
    """
    Find First N Armstrong Numbers
    Prints the first N Armstrong numbers.
    """
    count = 0
    num = 1
    armstrong_numbers = ""
    while count < n:
        num_str = str(num)
        num_digits = len(num_str)
        sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
        if sum_of_powers == num:
            armstrong_numbers += str(num) + " "
            count += 1
        num += 1
    return armstrong_numbers.strip()


def convert_to_binary(number):
    """
    Convert a Number to Binary (Without Using Built-in Functions)
    Asks the user for a number and converts it to binary using a loop.
    """
    if number == 0:
        return "Binary: 0"

    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary  # Prepend the remainder
        number //= 2
    return f"Binary: {binary}"


def print_pyramid_pattern(n):
    """
    Print Pyramid Pattern
    Prints the following pattern for N rows using loops.
    """
    output = ""
    for i in range(1, n + 1):
        spaces = "  " * (n - i)
        stars = "* " * (2 * i - 1)
        output += spaces + stars + "\n"
    return output
