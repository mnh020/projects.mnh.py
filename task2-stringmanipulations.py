# Task 1: Create a string `text` with the value "Python programming is powerful and versatile."
text = "Python programming is powerful and versatile."

# Perform the string operations and print the results

# Extract and print the substring "programming" using slicing.
substring = text[7:18]
print("Extracted substring:", substring)

# Split the string into a list of words.
words_list = text.split()
print("List of words:", words_list)

# Join the list of words back into a single string using a hyphen `-` as a separator.
hyphen_joined_string = "-".join(words_list)
print("Hyphen-joined string:", hyphen_joined_string)

# Task 2: Create a list `numbers` containing the elements: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100].
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Use list comprehension to create a new list `squares` containing the squares of each element in `numbers`.
squares = [number ** 2 for number in numbers]

# Print the `squares` list.
print("List of squares:", squares)
