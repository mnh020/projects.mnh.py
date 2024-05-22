# Exercise 1: Check if a letter is a vowel
def is_vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        print("This is a vowel.")
    else:
        print("This is not a vowel.")

# Example 1
letter = "a"
is_vowel(letter)

# Example 2
letter = "b"
is_vowel(letter)
