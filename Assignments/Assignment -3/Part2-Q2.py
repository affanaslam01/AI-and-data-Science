#2.Write a code to separate strings, numbers and Boolean data from the above list into separate lists.
my_List=["Tahir",44,"AI and data Science",True]
my_string=[]
my_number=[]
my_boolean=[]
for item in my_List:
    if type(item)==str:
       my_string.append(item)
    elif type(item)==int:
        my_number.append(item)
    elif type(item)==bool:
        my_boolean.append(item)
print("Strings:",my_string)
print("Numbers:",my_number)
print("Boolean:",my_boolean)
