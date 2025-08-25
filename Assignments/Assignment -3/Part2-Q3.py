#3.	Create a list [“apple”, “raspberry”, “pineapple”, “cherry”]. 
#a.	 How can you check if apple is present in the list and get the index of the element (if present)
#b.	Now replace the raspberry and pineapple with orange.
#c.	Insert “apricot” at index 2.
#d.	Extend the resulting list with items “car”, “bike”, “aeroplane”.
my_list=["apple","raspberry","pineapple","cherry"]
print(my_list.count("apple"))
print(my_list.index("apple"))
my_list[1:3]=["orange"]
my_list.insert(2,"apricot")
my_list.extend(["car","bike","aeroplane"])
print(my_list)
