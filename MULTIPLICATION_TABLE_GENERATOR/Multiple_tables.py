number = int(input("Enter a number: "))

for num in range(1, 6):
    print("\nTable for", num)

    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
