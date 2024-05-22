# Exercise 1: Check if a list is empty or not
def check_list_empty(my_lst):
    if len(my_lst) == 0:
        print("This list is empty!")
    else:
        print("This list is not empty!")

# Example 1
my_lst1 = []
check_list_empty(my_lst1)

# Example 2
my_lst2 = [6, 6, 3, 2, 4, 5, 5]
check_list_empty(my_lst2)
