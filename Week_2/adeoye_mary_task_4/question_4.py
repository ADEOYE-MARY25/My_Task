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










