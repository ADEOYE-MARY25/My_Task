# Electricity Bil Formatter
customer_name= input("kindly input your full name")
units_consumed = int(input ("kindly input the unit consumed"))
cost_per_unit = float(input("kindly input the cost_per_unit"))
total_bill = units_consumed +  cost_per_unit
print(total_bill)
print(f"Welcome {customer_name}, the unit consumed in your area is {units_consumed}, also the cost per unit consumed is {cost_per_unit}, finally yor total bill is {total_bill}")