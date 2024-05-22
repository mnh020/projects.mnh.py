# Exercise 1: Turn two sets into one dictionary
def sets_to_dict(set_1, set_2):
    if len(set_1) != len(set_2):
        print("Sets are not of the same size.")
        return
    my_dict = dict(zip(set_1, set_2))
    print(f"The dictionary is: {my_dict}")

# Example 1
set_1a = {1, 2, 3, 4}
set_2a = {7, 8, 9, 10}
sets_to_dict(set_1a, set_2a)

# Example 2
set_1b = {"one", "two", "three", "four"}
set_2b = {1, 2, 3, 4}
sets_to_dict(set_1b, set_2b)
