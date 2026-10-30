# Project: Expense Tracker - Installment 4
# Author: Kier Justine Baldomero
# Description: Prompts the user for two expenses, calculates subtotal, average, tax, grand total, and tracks budget with verdict messages.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("   Know where your money goes.")
print("=" * 40)

print("MAIN MENU")
print(f"[1] {'Add an expense':<20} (coming soon)")
print(f"[2] {'View all expenses':<20} (coming soon)")
print(f"[3] {'Show total spent':<20} (coming soon)")
print(f"[4] {'Exit':<20} (coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

# 2. Mag start po yung subtotal sa 0
subtotal = 0

# First expense
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
# i-update po yung subtotal after reading the amount (subtotal named only once per update)
subtotal = subtotal + amount1

# Print size message for the first amount
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Second expense
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
# i-update po ulit yung subtotal after reading the amount
subtotal = subtotal + amount2

# Print size message for the second amount
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Print two-big warning if both amounts exceed 100
if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

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

# Verdict logic (Exactly one verdict line, no negative amounts)
if over_budget:
    excess = total - budget
    print(f"Over budget by ${excess}!")
elif total > (budget * 0.90):
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)

print(f"Made by: Kier Justine Baldomero  |  Installment 4")