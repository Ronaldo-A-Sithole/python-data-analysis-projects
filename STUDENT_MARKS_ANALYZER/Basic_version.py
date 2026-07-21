marks = []

n = int(input("How many students? "))

for i in range(n):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("\n--- Results ---")
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)