#Write a program to take two numbers and an operator (/,x,+,-) as input and perform the corresponding operation.
num_1=int(input("Enter number 1: "))
num_2=int(input("Enter number 2: "))
operator=(input("Enter an operator: "))
if operator=="/":
    print(num_1/num_2)
elif operator=="*":
    print(num_1*num_2)
elif operator=="+":
    print(num_1+num_2)
elif operator=="-":
    print(num_1-num_2)
else:
    print("Invalid operator")
