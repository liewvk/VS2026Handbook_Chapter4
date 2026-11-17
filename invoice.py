unit_price = 36.50
quantity = 4
sales_tax_rate = 0.06
subtotal = unit_price * quantity
tax = round(subtotal * sales_tax_rate, 2)
total = subtotal + tax
print(f'Subtotal: RM{subtotal:.2f}')
print(f'Tax: RM{tax:.2f}')
print(f'Total: RM{total:.2f}')

