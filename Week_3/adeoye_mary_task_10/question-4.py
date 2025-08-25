# Task4
# Name Organizer
# names = []
#for m in range(2):
list_of_names =input("kindly input 5 names seperated by space: ")
# create case converter
create_case_converter= list_of_names.lower()
#sort the list
splitter = create_case_converter.split()
splitter.sort()
print(*splitter, sep="\n")


number_of_names = len(list_of_names)
# list_of_names = input("kindly input 5 names seperated by comma:")
# create_case_converter = list_of_names.lower()
# name= list_of_names >=5
if number_of_names  != 5:
    print("This names are incomplete,kindly check and update it")
else:
    print(f"here are your names{list_of_names}")


# This is a case of multiple exception

try:
    number = len("5")   # ValueError

except ValueError:
    print("Incomplete names check and make corrections.")

except ZeroDivisionError:
    print(" here are  your correct names")
