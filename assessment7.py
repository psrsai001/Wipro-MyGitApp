# The Grand Escape Room Challenge 🏰🔍
# Scenario:
# You and your team are trapped inside a mysterious escape room 🏰!
# To unlock the exit door, you must solve different puzzles using lists, tuples, sets, and dictionaries.
# Each puzzle tests a different concept of Python’s data structures. The final challenge requires you to combine all the concepts to escape!
#
#
# 🔎 Given Data (Game Elements)
# List of Clues Found in the Room
# These are the hidden clues found in different parts of the escape room. Some clues repeat.

clues_found = ["key", "map", "torch", "key", "note", "map", "compass", "torch"]

# Tuple of Puzzle Codes on the Wall
# The ancient puzzle codes are carved into the walls. They are stored in a tuple (unchangeable).

puzzle_codes = (312, 789, 456, 123, 654, 789)

# Set of Secret Symbols Discovered
# The secret symbols were found in different books inside the room. Since symbols cannot repeat, they are stored in a set.

secret_symbols = {"@", "#", "$", "&", "%", "@"}

# Dictionary of Lock Mechanisms and Their Solutions
# The final door has multiple locks. Each lock requires a unique solution to unlock.

lock_mechanisms = {
    "Alpha Lock": "312",
    "Beta Lock": "torch",
    "Gamma Lock": "@",
    "Delta Lock": "golden_key",
}

# 🕵️ Your Tasks (Solve these using Python Concepts)
# 1️⃣ Find Unique Clues – Remove duplicate clues and print the unique items found in the escape room. (Use a set)
unique_clues = set(clues_found)
print(unique_clues)


# 2️⃣ Verify If a Puzzle Code Exists –
# Ask the user to enter a 3-digit number.
# Check if it exists in the tuple of puzzle codes.
# Print "Valid Code" if it exists, otherwise print "Invalid Code".
n = input("Enter a 3 digit number: ")
if len(n) != 3:
    print("number is not a 3 digit number")
else:
    if int(n) in puzzle_codes:
        print("Valid Code")
    else:
        print("Invalid Code")

# 3️⃣ Compare Clues with Locks –
# Some clues may match the lock solutions.
# Compare unique clues found with lock mechanisms and print any matching clues.

matching_clues = [clue for clue in unique_clues if clue in lock_mechanisms.values()]
print("Matched clues:", matching_clues)

# 4️⃣ Match Secret Symbols with Locks –
# Some secret symbols may be needed to open locks.
# Find which symbols in the set match lock requirements and print them.

matching_symbols = [
    symbol for symbol in secret_symbols if str(symbol) in lock_mechanisms.values()
]
print("Matched Symbols:", matching_symbols)

# 5️⃣ Find the Missing Key –
# One of the locks requires a golden key, but it is not in the list of clues!
# Check if "golden_key" is in the clues list.
# If not, add it and print the updated clues list.

if "golden_key" not in unique_clues:
    unique_clues.add("golden_key")

# 6️⃣ Final Door Unlock –
# If at least 3 out of 4 locks are solved using clues, codes, or symbols, the door opens.
# Print "🎉 Escape Successful!" if the conditions are met.
# Otherwise, print "🚪 Still locked! Find more clues!".

if len(matching_clues) + len(matching_symbols) >= 2:
    print("🎉 Escape Successful!")
else:
    print("🚪 Still locked! Find more clues!")
