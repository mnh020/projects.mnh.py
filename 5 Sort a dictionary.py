# Exercise 5: Sort a dictionary by its values in ascending order
def sort_dict_by_values(my_dict):
    sorted_items = sorted(my_dict.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_items}
    print(f"The sorted dictionary is: {sorted_dict}")

# Example 1
my_dict1 = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
sort_dict_by_values(my_dict1)

# Example 2
my_dict2 = {0: 45, 1: 7, 2: 44, 3: 81, 4: 6}
sort_dict_by_values(my_dict2)
