#Write a function to take three numbers as argument and return the largest number.
def function(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
result= function(100,50,92)
print("The largest number is:",result)
