# Exercise 3.2: Alternate the elements between the two tuples
def alternate_elements_into_tuples(my_lst):
    tuple_1 = tuple(my_lst[i] for i in range(len(my_lst)) if i % 2 == 0)
    tuple_2 = tuple(my_lst[i] for i in range(len(my_lst)) if i % 2 != 0)
    print(f"Tuple 1 is: {tuple_1}")
    print(f"Tuple 2 is: {tuple_2}")

# Example 1
my_lst1 = [6, 2, 7, 4, 3]
alternate_elements_into_tuples(my_lst1)

# Example 2
my_lst2 = ['a', 'b', 'c', 1, 2, 3, 4, 'd', 5, "hello"]
alternate_elements_into_tuples(my_lst2)
