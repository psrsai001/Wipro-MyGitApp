
# Question 1: The Magic Number
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))
age = current_year - birth_year
print(f"You are {age} years old!")

# Question 2: Funny Name Switcheroo
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Your name in reverse order: {last_name} {first_name}")

# Question 3: The Mysterious Equation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Product: {num1 * num2}")
print(f"Difference: {num1 - num2}")

# Question 4: The Echo Machine
word = input("Enter a word: ")
repeat = int(input("Enter a number: "))
print(word * repeat)

# Question 5: Fast & Furious Speed Calculator
distance = float(input("Enter distance (km): "))
time = float(input("Enter time (hours): "))
speed = distance / time
print(f"Your speed is {speed} km/h")

# Question 6: The Dice Roller Simulator
random_number = int(input("Enter a random number: "))
print(f"Bitwise AND with 6 gives: {random_number & 6}")

# Question 7: Slot Machine - Modulus Magic
number = int(input("Enter a number: "))
print(f"Remainder when divided by 7: {number % 7}")

# Question 8: Temperature Converter
temp_celsius = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {temp_fahrenheit}°F")

# Question 9: Python Math Fun - Power Play
base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))
print(f"{base} raised to the power {exponent} is: {base ** exponent}")
