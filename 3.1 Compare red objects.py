# Exercise 3.1: Compare red objects set with fruits set and find red fruits
red_objects = {"apple", "crab", "rose", "strawberry"}
fruits = {"orange", "apple", "strawberry", "grape", "kiwi", "mandarin"}

red_fruits = red_objects & fruits
non_red_fruits = fruits - red_fruits

print(f"Red fruits: {red_fruits}")
print(f"Non-red fruits: {non_red_fruits}")
