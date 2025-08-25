#Write a function to compute factorial of a given number using recursion technique.
def fact(number):
    if number==0 or number==1:
        return 1
    else:
        result=number*fact(number-1)
        return result
print(fact(5))
result=fact(5)
print(f"Factorial of 5 is:",result)
