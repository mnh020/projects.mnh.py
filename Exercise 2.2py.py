# Exercise 2: Print a string using three different methods
first_string = "I am unwritten, "
second_string = "can’t read my mind, "
third_string = "I’m undefined."

# Using f-string
output_fstring = f"{first_string}{second_string}{third_string}"
print(output_fstring)

# Using concatenation
output_concatenation = first_string + second_string + third_string
print(output_concatenation)

# Using .format method
output_format = "{}{}{}".format(first_string, second_string, third_string)
print(output_format)
