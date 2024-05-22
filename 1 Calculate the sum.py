# Exercise 1: Calculate the sum of all numbers from 1 to a certain number
def sum_of_numbers(num):
    total = sum(range(1, num + 1))
    print(f"The sum is: {total}")

# Example 1
num1 = 5
sum_of_numbers(num1)

# Example 2
num2 = 3
sum_of_numbers(num2)

# Exercise 2: Generate the multiplication table of a number from 1 to 10
def multiplication_table(num):
    table = [num * i for i in range(1, 11)]
    print(f"The table is: {table}")

# Example 1
num3 = 5
multiplication_table(num3)

# Example 2
num4 = 3
multiplication_table(num4)

# Exercise 3: Find numbers between 2950 and 5210 that are multiples of 13 and 9
multiples = [num for num in range(2950, 5211) if num % 13 == 0 and num % 9 == 0]
print("Multiples of 13 and 9 between 2950 and 5210:", multiples)

# Exercise 4: Count even and odd digits in a number
def count_even_odd_digits(number):
    even_count = sum(1 for digit in str(number) if int(digit) % 2 == 0)
    odd_count = len(str(number)) - even_count
    print(f"This number has {odd_count} odd digits and {even_count} even digits")

# Example 1
num5 = 56472749
count_even_odd_digits(num5)

# Example 2
num6 = 135
count_even_odd_digits(num6)

# Exercise 5.1: Validate user password
def create_valid_password():
    while True:
        password = input("Create a password: ")
        if 4 <= len(password) <= 6 and password.isalpha():
            print("Valid password")
            return password
        else:
            print("That does not fulfill the requirements, try again")

def authenticate_password(correct_password):
    while True:
        entered_password = input("Enter your password: ")
        if entered_password == correct_password:
            print("That is correct")
            break
        else:
            print("That is incorrect, try again")

# Example
valid_password = create_valid_password()
authenticate_password(valid_password)

# Exercise 5.2: Encrypt user password with a given shift
def encrypt_password(password, shift):
    encrypted = ''.join(chr(ord(char) + shift) if char.isalpha() else char for char in password)
    print(f"Encrypted password: {encrypted}")

# Example 1
password1 = "friend"
shift1 = 1
encrypt_password(password1, shift1)

# Example 2
password2 = "sting"
shift2 = 4
encrypt_password(password2, shift2)
