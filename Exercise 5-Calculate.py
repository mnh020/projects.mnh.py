# Exercise 5: Calculate income after taxes
def calculate_after_taxes(income):
    if income < 67000:
        after_taxes = income * 0.76
    elif income < 97000:
        after_taxes = income * 0.69
    else:
        after_taxes = income * 0.66

    print(f"Your income after taxes is {after_taxes:.2f} euros")

# Example 1
calculate_after_taxes(58200)

# Example 2
calculate_after_taxes(101000)
