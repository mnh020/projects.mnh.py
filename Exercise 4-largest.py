# Exercise 4: Find the largest of 4 numbers
def find_largest(first_number, second_number, third_number, fourth_number):
    largest_number = max(first_number, second_number, third_number, fourth_number)
    print(f"The largest number is {largest_number}")

# Example 1
find_largest(10, 12, 8, 24)

# Example 2
find_largest(10, 10, 10, 4)
