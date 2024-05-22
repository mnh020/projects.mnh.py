# Exercise 5.1: Calculate the average of a list containing 5 elements
def calculate_average(my_lst):
    if len(my_lst) == 5:
        avg = sum(my_lst) / len(my_lst)
        print(f"The average is {avg}")
    else:
        print("The list does not contain 5 elements")

# Example 1
my_lst1 = [2, 2, 3, 3, 4]
calculate_average(my_lst1)

# Example 2
my_lst2 = [7, 7, 2, 2, 3]
calculate_average(my_lst2)
