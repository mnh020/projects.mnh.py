# Exercise 6: Check if a number or string is a palindrome
def is_palindrome(value):
    str_value = str(value)
    if str_value == str_value[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

# Example 1
number1 = 191
is_palindrome(number1)

# Example 2
number2 = 192
is_palindrome(number2)

# Example with a string
string = "radar"
is_palindrome(string)
