# Prompt the user for their monthly income
monthly_income = input("Enter your monthly income: ")

# Prompt the user for their total monthly expenses
total_monthly_expenses = input("Enter your total monthly expenses: ")

# Calculate the monthly savings
monthly_savings = float(monthly_income) - float(total_monthly_expenses)

# Assume an annual interest rate of 5%
annual_interest_rate = 0.05

# Calculate the projected savings after one year with interest
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Print the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")