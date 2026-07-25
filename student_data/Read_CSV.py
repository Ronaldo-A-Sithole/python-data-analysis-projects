#Read CSV (no pandas yet)

file = open("student_data/students.csv", "r")
lines = file.readlines()
file.close()

print(lines)

#Clean data

data = []

for line in lines[1:]:  # skip header
    parts = line.strip().split(",")

    if len(parts) < 3:
        continue

    name = parts[0]
    math = int(parts[1])
    science = int(parts[2])

    data.append([name, math, science])

#Analyze data

total_math = 0
top_student = ""
highest = 0

for student in data:
    name, math, science = student

    total_math += math

    if math > highest:
        highest = math
        top_student = name

average_math = total_math / len(data)

print("Average Math:", average_math)
print("Top Student:", top_student, "-", highest)

#Add insights
for student in data:
    name, math, science = student

    if math >= 75:
        print(name, "- Strong in Math")
    else:
        print(name, "- Needs improvement")