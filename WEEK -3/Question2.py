'''
Savings Goal Tracker:
Input the target savings goal and the current savings amount.
Ask for the monthly saving amount.
Calculate and display how many months it will take to reach the goal.
'''
target_savings = float(input("Enter your target savings goal: "))

current_savings = float(input("Enter your current savings amount: "))

monthly_savings = float(input("Enter the amount you plan to save each month: "))

remaining_savings = target_savings - current_savings

# Calculate how many months it will take to reach the goal
if monthly_savings > 0:
    months_to_goal = remaining_savings / monthly_savings
    print(f"\nIt will take approximately {months_to_goal:.2f} months to reach your savings goal.")
else:
    print("\nMonthly savings must be greater than 0 to reach your goal.")
