# Exercise 5: Print a string made of the first 3 and last 3 characters of a given string
def first_and_last_three(string):
    if len(string) < 3:
        result = string * 2
    else:
        result = string[:3] + string[-3:]
    print(result)

# Example 1
string1 = "Hello World"
first_and_last_three(string1)

# Example 2
string2 = "hey"
first_and_last_three(string2)
