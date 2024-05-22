# Exercise 2: Check if a key is in a dictionary and add it if not
def check_and_add_key(my_dict, key):
    if key in my_dict:
        print(f"{key} is in the dictionary!")
    else:
        my_dict[key] = "empty"
        print(f"{key} is not in the dictionary!")
        print(f"The new dictionary is: {my_dict}")

# Example 1
my_dict1 = {"dad": "Eise", "sister_1": "Iris", "sister_2": "Nicky"}
key1 = "dad"
check_and_add_key(my_dict1, key1)

# Example 2
my_dict2 = {"fruit": "Apple", "vegetable": "Capsicum"}
key2 = "meat"
check_and_add_key(my_dict2, key2)
