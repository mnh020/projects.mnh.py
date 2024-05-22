# Exercise 4: Sort a list of tuples by the second element
def sort_list_of_tuples(my_lst):
    sorted_lst = sorted(my_lst, key=lambda x: x[1])
    print(f"The ordered list is: {sorted_lst}")

# Example 1
my_lst1 = [(3, 2), (3, 1), (4, 3), (3, 4), (3, 5)]
sort_list_of_tuples(my_lst1)

# Example 2
my_lst2 = [(5, 2), (6, 1), (4, 2), (3, 4), (7, 5)]
sort_list_of_tuples(my_lst2)
