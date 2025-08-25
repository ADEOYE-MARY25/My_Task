# Online Store Cart Calculation
# create a list of items (e.g., "Book", "pen", "Bag") and another list of prices (e.g., 500, 100, 2000)
items=  ["Book", "pen", "Bag"]
price =[500, 100, 2000]

# Start with a empty cart total = 0).
cart_total = 0

# Use assignment operators (+=) to add the price of some items into cart_total.
cart_total+= price[0]
cart_total+=price[1]
cart_total+=price[2]
print(cart_total)

#print the list of items and the total price using an f-string like this:
print(f"the list of items:{items} and total price:{cart_total}")


if "Car" in items: 
   print("this are the price  items for your shopping")
else:
    print("this is not included in your shopping list")



