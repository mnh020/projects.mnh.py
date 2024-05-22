# Exercise 3.2: Combine red and orange fruits, exclude non-fruits
orange_objects = {"basketball", "fanta", "orange", "autumn leaves", "mandarin"}

red_and_orange_fruits = (red_objects | orange_objects) & fruits
non_fruit_objects = (red_objects | orange_objects) - fruits

print(f"Red and orange fruits: {red_and_orange_fruits}")
print(f"Non-fruit objects: {non_fruit_objects}")
