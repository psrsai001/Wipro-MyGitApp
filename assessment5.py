def print_numbers_1_to_n():
    """
    Print Numbers from 1 to N
    Asks the user for a number N and prints numbers from 1 to N using a loop.
    """
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        print(i, end=", ")


def print_even_numbers_1_to_n():
    """
    Print Even Numbers from 1 to N
    Asks the user for a number N and prints all even numbers from 1 to N.
    """

    n = int(input("Enter a number: "))
    for i in range(2, n + 1, 2):
        print(i, end=", ")


def sum_of_first_n_natural_numbers(n):
    """
    Sum of First N Natural Numbers
    Asks the user for a number N and finds the sum of the first N natural numbers.
    """
    n = int(input("Enter a number: "))
    print(f"Sum: {n*(n + 1)/2}")


def reverse_counting_n_to_1():
    """
    Reverse Counting from N to 1
    Asks the user for a number N and prints numbers in reverse from N to 1.
    """

    n = int(input("Enter a number: "))
    for i in range(n, 0, -1):
        print(i, end=", ")


def multiplication_table():
    """
    Multiplication Table of a Given Number
    Asks the user for a number X and prints its multiplication table up to 10.
    """

    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")


def count_digits():
    """
    Count Digits of a Number
    Asks the user for a number and counts the total number of digits using a loop.
    """
    n = input("Enter a number: ")
    print("Len: ", len(n))


def reverse_number():
    """
    Reverse a Number
    Asks the user for a number and prints it in reverse order.
    """
    n = input("Enter a number: ")
    print("rev", n[::-1])


def factorial():
    """
    Factorial of a Number
    Asks the user for a number N and calculates its factorial.
    """
    n = int(input("Enter a number: "))
    if n == 0:
        return "Factorial: 1"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial: {fact}")


def fibonacci_series():
    """
    Fibonacci Series (First N Terms)
    Asks the user for N and prints the first N Fibonacci numbers.
    """

    n = int(input("Enter a number: "))
    if n <= 0:
        print("invalid range")
    elif n == 1:
        print("0")
    else:
        a, b = 0, 1
        output = "0 1"
        for _ in range(2, n):
            c = a + b
            output += " " + str(c)
            a, b = b, c
        print(output)


def sum_of_digits():
    """
    Find the Sum of Digits
    Asks the user for a number and finds the sum of its digits.
    """
    digit_sum = 0
    n = int(input("Enter a number: "))
    number = abs(n)  # handle negative numbers
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    print(f"Sum of digits: {digit_sum}")
