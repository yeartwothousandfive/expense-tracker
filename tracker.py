# Project: Expense Tracker - Installment 5
# Author: Kier Justine Baldomero
# Description: A menu-driven expense tracker that calculates subtotal, tax, grand total, and budget verdict.

# 1. Header at banner po, ipi-print isang beses lang sa umpisa
print("=" * 40)
print("\tEXPENSE TRACKER")
print("   Know where your money goes.")
print("=" * 40)

# 2. Tanungin po yung name, tax rate, at budget isang beses lang bago magsimula yung menu
name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

# I-initialize po yung mga variables para sa tracking
subtotal = 0
count = 0

# Main loop po: Ito po yung nagpapaulit-ulit ng menu hangga't hindi pinipili yung exit.
# Kailangan po ito kasi bawal i-copy paste yung menu text, dapat isang beses lang nakasulat sa code.
while True:
    # 3. Ipakita po yung MAIN MENU (ito lang po yung beses na naka-code yung menu)
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")
    
    # Kunin po yung choice as string para kahit 'abc' o '7' ang i-type, hindi mag-crash
    choice = input("Choose 1-4: ")
    
    # Option 1 po: Mag-add ng expense
    if choice == "1":
        amount = float(input("Amount? "))
        
        # I-update po yung subtotal after reading the amount (subtotal named only once per update)
        subtotal = subtotal + amount
        count = count + 1
        
        # Size-message decision po (naka-code lang isang beses)
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
            
    # Option 2 po: Coming soon message
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
        
    # Option 3 po: Ipakita yung total spent at verdict
    elif choice == "3":
        # Compute po yung tax at total
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total
        
        # I-print po yung summary na aligned (Expenses, Subtotal, Tax, Grand total)
        print(f"  Expenses:   {count}")
        print(f"  Subtotal:   ${subtotal}")
        print(f"  Tax ({tax_percent}%): ${tax}")
        print(f"  Grand total: ${total}")
        
        # Verdict logic po (Exactly one verdict line, no negative amounts)
        if total > budget:
            excess = total - budget
            print(f"  Over budget by ${excess}!")
        elif total > (budget * 0.90):
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")
            
    # Option 4 po: Exit na tayo, dito lang po dapat natatapos yung program
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Kier Justine Baldomero  |  Installment 5")
        print("=" * 40)
        break
        
    # Anything else po na hindi 1, 2, 3, o 4 (like 7 or abc)
    else:
        print("  Please choose 1, 2, 3 or 4.")