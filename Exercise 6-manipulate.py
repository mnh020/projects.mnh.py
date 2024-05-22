# Exercise 6: Do something different depending on the size of the string
def manipulate_string(s):
    if len(s) == 1:
        print(s * 6)
    elif len(s) == 2:
        print(s[::-1])
    elif len(s) == 3:
        print(s[-1] + s[:-1])
    elif len(s) == 4:
        print(s[::-1])
    elif len(s) == 5:
        print(f"{s[0]}t{s[1]}t{s[2]}t{s[3]}t{s[4]}")
    else:
        print("String length is out of the allowed range (1-5 characters).")

# Example 1
manipulate_string("a")

# Example 2
manipulate_string("at")

# Example 3
manipulate_string("Dog")

# Example 4
manipulate_string("Wait")

# Example 5
manipulate_string("Brain")
