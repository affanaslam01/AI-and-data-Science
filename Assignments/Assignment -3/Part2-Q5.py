#5.	Create a list [32,54,66,11,77,10,90]
#a.	Remove items from the list with values less than 20.
#b.	Sort the list in ascending and descending order.
#c.	Now, compute the average value of the list items.
L=[32,54,66,11,77,10,90]
for item in L:
    if item>=20:
        print(item)
L.sort()
print(L)
L.sort(reverse=True)
print(L)
sum=0
total_values=0
for i in L:
    sum+=i
    total_values+=1
average=sum/total_values
print("Average values:",average)
