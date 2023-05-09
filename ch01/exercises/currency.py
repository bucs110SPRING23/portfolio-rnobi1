rate = float(input("What is the exchange rate for Euros to USD? $"))
amount = float(input("How is the amount being exchanged? €"))
total = amount * rate
result = round(total - 3.00, 2)
print(f"Your converted amount is ${result}")