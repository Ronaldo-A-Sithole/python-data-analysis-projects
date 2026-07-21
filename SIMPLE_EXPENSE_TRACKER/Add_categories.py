expenses = {}

n = int(input("How many expenses? "))

for i in range(n):
    category = input("Enter category (food, transport, etc): ")
    amount = float(input("Enter amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

print("\n--- Expense Summary ---")

for category, total in expenses.items():
    print(category, ":", total)

highest_category = max(expenses, key=expenses.get)
print("\nHighest spending:", highest_category, "-", expenses[highest_category])