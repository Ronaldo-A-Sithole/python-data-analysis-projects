file = open("student_data/students.csv", "r")
lines = file.readlines()
file.close()

print(lines)
