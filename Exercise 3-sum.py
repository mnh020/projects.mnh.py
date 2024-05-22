# Exercise 3: Sum of 3 numbers with special condition
def sum_or_multiply(first_number, second_number, third_number):
    total_sum = first_number + second_number + third_number
    if first_number == second_number == third_number:
        print("These numbers are the same!")
        print(f"The sum of these numbers is {total_sum}")
        print(f"Multiplied by 4 this becomes {total_sum * 4}")
    else:
        print(f"The sum of these numbers is {total_sum}")

# Example 1
sum_or_multiply(10, 12, 8)

# Example 2
sum_or_multiply(10, 10, 10)
