students = {}

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    mark = float(input("Enter mark: "))
    students[name] = mark

print("\n--- Student Results ---")

for name, mark in students.items():
    if mark >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print(name, ":", mark, "-", status)