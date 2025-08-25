#	From the given list:
#Gadgets = [“Mobile”, “Laptop”, 10.0, “Marker”, 3, 10, “Speakers”, “Camera”, 310.25]
#a.	Create separate list of string and numbers,
#b.	Sort the string list in ascending and descending order
#c.	Sort the string list by length of elements in the list
#d.	Sort the numbers list in ascending and descending order
Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]
my_string=[]
my_numbers=[]
for item in Gadgets:
    if type(item)==str:
        my_string.append(item)
    else:
        my_numbers.append(item)
print("String:",my_string)
print("Numbers:",my_numbers)
my_string.sort()
print(my_string)
my_string.sort(reverse=True)
print(my_string)
my_string.sort(key=len)
print(my_string)
my_numbers.sort()
print(my_numbers)
my_numbers.sort(reverse=True)
print(my_numbers)
