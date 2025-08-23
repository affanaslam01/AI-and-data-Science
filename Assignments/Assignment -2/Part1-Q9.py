#Write a program that ask for an integer number and checks if it is divisible by 2, 3, or both.
num=int(input("Enter an integer number: "))
if num%2==0 and num%3==0:
    print("number is divisible by both")
elif num%2==0:
    print("number is divisible by 2")
elif num%3==0:
    print("number is divisible by 3")
else:
    print("number is not divisible by 2 and 3")
