expenses = []

n = int(input("How many expenses? "))

for i in range(n):
    amount = float(input(f"Enter expense {i+1}: "))
    expenses.append(amount)

total = sum(expenses)
print("Total spent:", total)