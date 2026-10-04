# Project: Expense Tracker - Installment 3
# Author: Kier Justine Baldomero
# Description: Prompts the user for two expenses, calculates subtotal, average, tax, grand total, and tracks budget.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("   Track your expenses easily.")
print("=" * 40)

print("MAIN MENU")
print(f"1. {'Add an expense':<20} (coming soon)")
print(f"2. {'View all expenses':<20} (coming soon)")
print(f"3. {'Show total spent':<20} (coming soon)")
print(f"4. {'Exit':<20} (coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

# 2. Mag start po yung subtotal sa 0
subtotal = 0

# First expense
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
# i-update po yung subtotal after reading the amount (subtotal named only once per update)
subtotal = subtotal + amount1

# Second expense
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
# i-update po ulit yung subtotal after reading the amount
subtotal = subtotal + amount2

# 3. Compute po yung average sa subtotal 
average = subtotal / 2

# 4. Ask for tax rate as a whole number then compute sa tax and grand total
tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

# 5. Ask for a budget then store whether grand total is over budget
budget = float(input("Your budget? "))
over_budget = total > budget  # Computed from variables, not hardcoded

# 6. Compute what is left in budget
left = budget - total

# 7. SUMMARY lines
print("-" * 40)
print("SUMMARY")
# 8. Values lined up with \t
print(f"- {item1}:\t${amount1}")
print(f"- {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

print(f"Made by: Kier Justine Baldomero  |  Installment 3")