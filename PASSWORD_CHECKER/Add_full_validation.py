password = input("Enter password: ")

has_upper = False
has_number = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_number = True

if len(password) >= 8 and has_upper and has_number:
    print("Strong password")
else:
    print("Weak password")