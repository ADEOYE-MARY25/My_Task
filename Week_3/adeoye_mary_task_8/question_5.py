# Task5
# Create a dictionary called store with items and thier available  quantities.
store  = {"milk": 150, "cup": 200, "shoe": 300}
# Ask the user to input the  tems they want to buy 
items = input("Kindly input the items you want to buy: ")
quantity = int(input("kindly input the quantity you want to purchase"))
store[items] += quantity
print("updated store", store)




