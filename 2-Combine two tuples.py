# Exercise 2: Combine two tuples into one tuple
def combine_tuples(tuple_1, tuple_2):
    new_tuple = tuple_1 + tuple_2
    print(f"The new tuple is: {new_tuple}")

# Example 1
tuple_1a = (1, 2, 3)
tuple_2a = (4, 5, 6)
combine_tuples(tuple_1a, tuple_2a)

# Example 2
tuple_1b = (2, 3, 7, 4)
tuple_2b = (7, 1)
combine_tuples(tuple_1b, tuple_2b)
