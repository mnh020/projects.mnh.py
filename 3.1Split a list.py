# Exercise 3.1: Split a list into two tuples of the same size
def split_list_into_tuples(my_lst):
    mid_index = len(my_lst) // 2
    tuple_1 = tuple(my_lst[:mid_index])
    tuple_2 = tuple(my_lst[mid_index:])
    print(f"Tuple 1 is: {tuple_1}")
    print(f"Tuple 2 is: {tuple_2}")

# Example 1
my_lst1 = [6, 2, 7, 4, 3]
split_list_into_tuples(my_lst1)

# Example 2
my_lst2 = ['a', 'b', 'c', 1, 2, 3, 4, 'd', 5, "hello"]
split_list_into_tuples(my_lst2)
