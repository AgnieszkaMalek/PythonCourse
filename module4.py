# Import the necessary module for generating random numbers.
import random

# Create a variable named random_number and assign it a random integer between 1 and 100.
random_number = random.randint(1, 100)

# Print the random number along with its data type using the type() function, use double and single quote.
print("The random number is:", random_number)
print('The type of the random number is:', type(random_number))

# Ensure that your variables are using multi-word variable naming conventions such as camel case, pascal case, or snake case
multiWordVariableCamelCase = "ThisIsCamelCase"
multi_word_variable_pascal_case = "ThisIsPascalCase"
multi_word_variable_snake_case = "this_is_snake_case"

# Experiment with type conversions by converting the random number to a float and then to a complex number.
random_number_float = float(random_number)
print("The random number as a float is:", random_number_float)
print('The type of the random number as a float is:', type(random_number_float))

# Convert the random number to a complex number and print its value and type
random_number_complex = complex(random_number)
print("The random number as a complex number is:", random_number_complex)
print('The type of the random number as a complex number is:', type(random_number_complex))


