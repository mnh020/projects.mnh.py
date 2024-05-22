# Exercise 3: Convert a list of characters into a string
def list_to_string(my_lst):
    if len(my_lst) == 5:
        result_string = ''.join(my_lst)
        print(f"The string is: {result_string}")
    else:
        print("This list doesn’t have the right size")

# Example 1
my_lst1 = ['h', 'e', 'l', 'l', 'o']
list_to_string(my_lst1)

# Example 2
my_lst2 = ['h', 'e', 'y']
list_to_string(my_lst2)
