#Write a program to find the largest of the three numbers.
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
if num1>num2 and num1>num3:
    print("Number 1 is larger")
elif num2>num1 and num2>num3:
    print("Number 2 is larger")
else:
    print("Number 3 is larger")
