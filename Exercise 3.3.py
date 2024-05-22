# Exercise 3: Check if a string is longer or shorter than 10 characters
def check_string_length(sentence):
    if len(sentence) > 10:
        print("This string is longer than 10 characters")
    else:
        print("This string is shorter than 10 characters")

# Example 1
sentence1 = "I am a super long sentence"
check_string_length(sentence1)

# Example 2
sentence2 = "short"
check_string_length(sentence2)
