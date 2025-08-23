#Write a program to compute the factorial of a number using while loop.
number=int(input("enter a number:"))
factorial=1
i=number
while (i>0):
    factorial=factorial*i
    i-=1
print(f"factorial of {number} is:",factorial)
