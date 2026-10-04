# Project: Expense Tracker - Installment 2
# Author: Kier Justine Baldomero
# Description: Prompts the user for two expenses, calculates the total and average, and prints a formatted summary.

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
# The <13 alignment ensures the dollar signs line up in one column
print(f"- {item1 + ':':<13} ${amount1}")
print(f"- {item2 + ':':<13} ${amount2}")
print(f"{'Total spent:':<13} ${total}")
print(f"{'Average:':<13} ${average}")
print("-" * 40)

print(f"Made by: Kier Justine Baldomero  |  Installment 2")