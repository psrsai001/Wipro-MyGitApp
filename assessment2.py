# 🧩 Question 11: Circle Calculator 🟠
# Write a Python program that asks the user for the radius of a circle and calculates the area and circumference.
# 🔹 Hint:
# Use the formula:
# Area: A=π×r*r
# Circumference: C=2×π×r

# 📌 Example Input:
# Enter the radius of the circle: 5


# 📌 Example Output:
#
# Area: 78.5
# Circumference: 31.4
def area_of_circle():
    r = int(input("Enter radius: "))
    print(f"Area3: {round(3.14*r*r, 2)}")
    print(f"Circumference: {round(2*3.14*r, 2)}")


# 🎵 Question 12: Double Trouble 🎶
# Ask the user for a number. Print the double of that number.
# 🔹 Hint:
# Use the * operator to double the number.
# 📌 Example Input:
#
# Enter a number: 7
#
# 📌 Example Output:
#
# Double of 7 is 14
def double_number():
    n = int(input("Enter a number: "))
    print(f"Double of {n} is {n * 2}")


# 🏋️ Question 13: Weight on the Moon 🌕
# Write a Python program that asks the user for their weight on Earth and calculates their weight on the Moon.
# 🔹 Hint:
# Weight on the Moon is about 16.5% of the weight on Earth.
# Use multiplication (*) to calculate this.
# 📌 Example Input:
#
# Enter your weight on Earth (kg): 60
#
# 📌 Example Output:
#
# Your weight on the Moon would be: 9.9 kg
def weight_in_moon():
    weight = int(input("Enter your weight on Earth (kg): "))
    print(f"Your weight on the Moon would be: {round(weight* 16.5 / 100, 1)} kg")


# 🏗️ Question 14: Simple Interest Calculator 💰
# Ask the user for the principal amount (P), rate of interest (R), and time (T) in years. Calculate the simple interest.
# 🔹 Hint:
# Use the formula: Simple Interest=P×R×T / 100
# 📌 Example Input:
#
# Enter principal amount: 1000
# Enter rate of interest: 5
# Enter time (years): 2
#
# 📌 Example Output:
#
# Simple Interest: 100.0
def simple_interest():
    p = int(input("Enter principal amount: "))
    r = int(input("Enter rate of interest: "))
    t = int(input("Enter time (years): "))
    print(f"Simple Interest: {round(p*t*r/100, 1)}")


# 🧮 Question 15: Sum of Digits 🧮
# Ask the user for a three-digit number and print the sum of its digits.
# 🔹 Hint:
# Use // and % operators to extract the digits.
# 📌 Example Input:
#
# Enter a three-digit number: 123
#
# 📌 Example Output:
#
# Sum of digits: 6
def three_digit_sum():
    n = input("Enter 3 digit num:")
    if len(n) != 3:
        print("input is not a 3 digit number")
    else:
        print("sum of digits:", int(n[0]) + int(n[1]) + int(n[2]))


# 🏃 Question 16: Marathon Pace Calculator 🏃‍♂️
# Ask the user for the distance (in miles) they plan to run and the time (in minutes) they want to finish in. Calculate their required pace (minutes per mile).
# 🔹 Hint:
# Use division (/) to calculate the pace.
# 📌 Example Input:
# Enter distance (miles): 5
# Enter time (minutes): 50
#
# 📌 Example Output:
#
# You need to run 10.0 minutes per mile.
def marathon_pase_calculator():
    dist = int(input("Enter distance (miles): "))
    time = int(input("Enter time (minutes): "))
    print(f"you need to run {round(dist/time, 1)} minutes per mile.")


# 🧪 Question 17: Chemistry Lab Mix 💧
# Ask the user for the volume of two solutions (in liters). Calculate and print the total volume and the average volume.
# 🔹 Hint:
# Use + for total volume and / for average volume.
# 📌 Example Input:
#
# Enter volume of solution 1 (liters): 2.5
# Enter volume of solution 2 (liters): 3.5
#
# 📌 Example Output:
# Total volume: 6.0 liters
# Average volume: 3.0 liters
def chemistry_lab():
    sol1 = float(input("Enter volume of solution 1 (liters): "))
    sol2 = float(input("Enter volume of solution 2 (liters): "))

    total = sol1 + sol2
    avg = round(total / 2, 1)
    print("Total volume:", total, "liters")
    print("Average volume:", avg, "liters")


# 🔢 Question 18: Number Manipulator 🔄
# Ask the user for a number. Print the square, cube, and the square root of that number.
# 🔹 Hint:
# Use ** for power calculations.
# Use **0.5 for the square root.
# 📌 Example Input:
# Enter a number: 4
#
# 📌 Example Output:
#
# Square: 16
# Cube: 64
# Square root: 2.0
def calculate_powers():
    n = int(input("Enter a number: "))
    sq = n**2
    cube = sq * n
    sqrt = round(n**1 / 2, 1)
    print("Square:", sq)
    print("Cube:", cube)
    print("Square root:", sqrt)


#
# 💡 Question 19: Light Year Converter 🚀
# Ask the user for a distance in kilometers and convert it to light years.
# 🔹 Hint:
# 1 light year = 9.461 trillion kilometers.
# Use division (/) for the conversion.
# 📌 Example Input:
#
# Enter distance in kilometers: 9461000000000
#
# 📌 Example Output:
#
# Distance in light years: 1.0
def light_years():
    distance = int(input("Enter distance in KM: "))
    light_year = 9461000000000
    print(f"Distance in light years: {round(distance / light_year, 1)}")


# 🎈 Question 20: Ball Volume Calculator 🎈
# Ask the user for the radius of a spherical ball and calculate its volume.
# 🔹 Hint:
# Use the formula: V=4/3 * pi * r * r * r
# Assume π=3.14
# 📌 Example Input:
#
# Enter the radius of the ball: 3
#
# 📌 Example Output:
#
# Volume: 113.04
def ball_volume():
    r = int(input("Enter radius: "))
    print(f"Volume: {round(4/3*3.14*r*r*r, 2)}")
