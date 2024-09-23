# Python script that takes a string as input and performs various string manipulation operations based on user choice.

# 1. Prompt the user to enter a string
user_input = input("Enter a text sentence: ")

# 2. Display a menu of string manipulation options:
print("\nString Manipulation Menu:")
print("1. Convert text sentence to uppercase")
print("2. Convert text sentence to lowercase")
print("3. Slice the text sentence")
print("4. Calculate all characters in the text sentence")
print("5. Show all characters")

# Prompt the user to enter a string.
choice = int(input("Enter your choice (1-5): "))

# Perform the selected string manipulation
if choice == 1:
    result = user_input.upper()
    print("Uppercase:", result)
elif choice == 2:
    result = user_input.lower()
    print("Lowercase:", result)
elif choice == 3:
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    result = user_input[start:end]
    print("Sliced part of the text:", result)
elif choice == 4:
    length = len(user_input)
    print("Text sentence length:", length)
elif choice == 5:
    print("Characters:")
    for char in user_input:
        print(char)
else:
    print("Invalid choice.")