#Write a program that checks if a given number is positive, negative or zero.
num=(input("Enter Number: "))
num=int(num)
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
