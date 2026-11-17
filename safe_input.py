def read_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a nonnegative amount.")
                continue
            return value
        except ValueError:
            print("Enter a number, such as 12.50")


print(f"Amount: {read_amount('Amount: '):.2f}")
