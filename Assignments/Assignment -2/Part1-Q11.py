#Write a program that evaluates if an input number is prime.
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime number")
            break
    else:
        print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
