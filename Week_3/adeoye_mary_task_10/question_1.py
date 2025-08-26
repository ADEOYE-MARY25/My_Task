# Stimulate USSD Menu Interaction
Introduction =print("Welcome to MTN customer service we are everwhere you go")
code = ("kindly dial *123# to check all our services" )
checked_balance =input ("kindly check your balance")
Buy_Airtime = input("kindly buy your airtime")
Buy_Data = input ("kindly buy your data service ") 
print(f" kindly check your balance {"checked_balance"}.\n buy your airtime {"Buy Airtime"}.\n and lastly to buy data press{"Buy_Data"} ")
Choose_offer = ("kindly choose an offer between {1,2,3} {Buy_Data}")


# if-else statement
checked_balance= 5000
Buy_Airtime= 1000

if checked_balance >= Buy_Airtime:
    print("PURCHASE SUCCESSFUL") 
else:
    print("INSUFFICIENT BALANCE")


    # Using try method
