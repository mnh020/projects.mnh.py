# Exercise 5.2: Add a number to the list that turns the average into 5
def add_number_to_average_5(my_lst):
    current_sum = sum(my_lst)
    required_sum = 5 * (len(my_lst) + 1)
    number_to_add = required_sum - current_sum
    my_lst.append(number_to_add)
    print(f"The average was {current_sum / len(my_lst[:-1])}")
    print(f"Added {number_to_add}, new list is {my_lst}")
    print(f"The average is now {sum(my_lst) / len(my_lst)}")

# Example 1
my_lst1 = [2, 2, 3, 3, 4]
add_number_to_average_5(my_lst1)

# Example 2
my_lst2 = [7, 7, 2, 2, 3]
add_number_to_average_5(my_lst2)
