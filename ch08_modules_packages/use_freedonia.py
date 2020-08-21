from freedonia import calculate_tax

tax_at_12noon = calculate_tax(100, 'Harpo', 12)
tax_at_9pm = calculate_tax(100, 'Harpo', 21)
 
print(f'Tax amount: {tax_at_12noon}')
print(f'Tax amount: {tax_at_9pm}')

invalid_time = calculate_tax(100, 'Harpo', -1)