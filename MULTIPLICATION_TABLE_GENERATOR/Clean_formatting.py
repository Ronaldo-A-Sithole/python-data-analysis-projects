number = int(input("Enter a number: "))

for num in range(1, 15):
    print(f"\n--- Table for {num} ---")

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
