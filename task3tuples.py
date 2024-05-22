# Task 3.1: Create a tuple `coordinates` with the values (34.0522, -118.2437)
coordinates = (34.0522, -118.2437)

# Print each element of the tuple
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# Task 3.2: Create a dictionary `student`
student = {
    'name': 'Alice',
    'age': 24,
    'courses': ['Math', 'Science', 'English']
}

# Add a new key-value pair 'graduated': False
student['graduated'] = False

# Update the 'age' value to 25
student['age'] = 25

# Print the dictionary
print("Student dictionary:", student)

# Task 3.3: Create a set `unique_numbers`
unique_numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}

# Add the number 6 to the set
unique_numbers.add(6)

# Remove the number 2 from the set
unique_numbers.remove(2)

# Check if the number 3 is in the set and print the result
is_three_in_set = 3 in unique_numbers
print("Is 3 in the set?", is_three_in_set)

# Print the set
print("Unique numbers set:", unique_numbers)
