# Exercise 2: Check if a number is between 1000 and 2000
def check_number_range(number):
    if 1000 <= number <= 2000:
        print("This number is in between 1000 and 2000")
    elif number < 1000:
        print("This number is lower than 1000")
    else:
        print("This number is higher than 2000")

# Example 1
number = 1420
check_number_range(number)

# Example 2
number = 12
check_number_range(number)
