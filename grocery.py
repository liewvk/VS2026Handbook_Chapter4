items = [('Rice', 35.0), ('Milk', 8.5), ('Tea', 15.0)]
subtotal = sum(amount for _, amount in items)
for name, amount in items:
    print(f"{name:<20} RM{amount:>8.2f}")
print(f"Subtotal: RM{subtotal:.2f}")
print(f"Largest cost: {max(items, key=lambda row: row[1])[0]}")

