# Task 4.1: Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Print all prime numbers between 1 and 50
primes = [n for n in range(1, 51) if is_prime(n)]
print("Prime numbers between 1 and 50:", primes)

# Task 4.2: FizzBuzz program
numbers = list(range(1, 16))

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
