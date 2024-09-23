# User Profile Generator

# 1. User information
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_age = input("Enter your age: ")
user_city = input("Enter your City: ")
user_occupation = input("Enter your occupation: ")


# 2. First and last name concatenation
print(f"Hello {user_first_name} {user_last_name}!")


# 3. Sentence includes user age, city and occupation
print(f"It is very impressive that as {user_age} years old you've got {user_occupation} position in {user_city}.")


#4. Escape characters to include quotation marks and a new line
print(f"{user_first_name}, did you know?\n Our manager said:\n \"You are the best {user_occupation} so far in our company\".")

#5. String methods to modify the full name and profile description
print("\n*****Employer Profile*****")
print(f"Full name: {user_first_name.capitalize()} {user_last_name.upper()}")
print(f"Occupation: {user_occupation.title()}")