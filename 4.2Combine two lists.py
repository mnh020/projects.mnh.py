# Exercise 4.2: Combine two lists and find the quarter with the most sick days
def find_sickest_quarter(sick_days_1, sick_days_2):
    if any(day < 0 for day in sick_days_1 + sick_days_2):
        print("Frank can’t be sick for negative days!")
        return
    
    full_list = sick_days_1 + sick_days_2
    print(f"The full list of Frank’s sick days is: {full_list}.")
    
    max_sick_days = max(full_list)
    max_quarter = full_list.index(max_sick_days) + 1
    
    if max_quarter <= 4:
        print(f"Frank was sick the most in quarter {max_quarter} of the first year.")
    else:
        print(f"Frank was sick the most in quarter {max_quarter - 4} of the second year.")

# Example 1
sick_days_1_1 = [10, 4, 5, 19]
sick_days_1_2 = [7, 8, 2, 12]
find_sickest_quarter(sick_days_1_1, sick_days_1_2)

# Example 2
sick_days_2_1 = [0, 4, 1, 2]
sick_days_2_2 = [3, 4, 0, 0]
find_sickest_quarter(sick_days_2_1, sick_days_2_2)
