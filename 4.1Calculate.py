# Exercise 4.1: Calculate how many days Frank went dancing last year
def calculate_dancing_days(sick_days):
    if any(day < 0 for day in sick_days):
        print("Frank can’t be sick for negative days!")
    else:
        total_sick_days = sum(sick_days)
        total_days_in_year = 365
        dancing_days = total_days_in_year - total_sick_days
        print(f"Frank was sick for {total_sick_days} days.")
        print(f"He went dancing for {dancing_days} days")

# Example 1
sick_days1 = [10, 4, 5, 19]
calculate_dancing_days(sick_days1)

# Example 2
sick_days2 = [0, 4, 1, -1]
calculate_dancing_days(sick_days2)
