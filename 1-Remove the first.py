# Exercise 1: Remove the first, third, and fourth numbers from a list if they are there
def remove_first_third_fourth(my_lst):
    indices_to_remove = [0, 2, 3]
    new_lst = [num for i, num in enumerate(my_lst) if i not in indices_to_remove]
    print(f"The new list is: {new_lst}")

# Example 1
my_lst1 = [1, 2, 3, 4, 5, 6]
remove_first_third_fourth(my_lst1)

# Example 2
my_lst2 = [1, 2, 3]
remove_first_third_fourth(my_lst2)
