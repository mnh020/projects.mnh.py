# Exercise 7: Basic test with three questions
def basic_test():
    questions = [
        ("What is 2 * 2?", 4),
        ("What is 6 / 3?", 2),
        ("What is 9 * 9?", 81)
    ]
    
    for question, correct_answer in questions:
        answer = int(input(question + " "))
        if answer == correct_answer:
            print("That is correct!")
        else:
            print("That is false, you failed the test!")
            return

    print("Correct! You passed the test!")

# Run the test
basic_test()
