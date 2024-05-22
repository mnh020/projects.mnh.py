# Exercise 4: Print the reverse of a string if its length is a multiple of 3
def reverse_if_multiple_of_three(sentence):
    print(f"This string is {len(sentence)} characters long")
    if len(sentence) % 3 == 0:
        print(sentence[::-1])
    else:
        print(sentence)

# Example 1
sentence1 = "I have 1 dog"
reverse_if_multiple_of_three(sentence1)

# Example 2
sentence2 = "Pizza"
reverse_if_multiple_of_three(sentence2)
