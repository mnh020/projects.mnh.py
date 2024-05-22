# Exercise 2: Reorder a list and remove the largest and smallest number from it
def reorder_and_remove_extremes(my_lst):
    if len(my_lst) > 2:
        my_lst.sort()
        new_lst = my_lst[1:-1]
        print(f"The new list is: {new_lst}")
    else:
        print("List is too short to remove extremes.")

# Example 1
my_lst1 = [6, 2, 7, 4, 3]
reorder_and_remove_extremes(my_lst1)

# Example 2
my_lst2 = [6, 6, 3, 2, 4, 5, 5]
reorder_and_remove_extremes(my_lst2)
