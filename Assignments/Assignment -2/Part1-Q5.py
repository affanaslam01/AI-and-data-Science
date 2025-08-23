#Write a program to take user’s age as input and display whether he is minor, adult or senior citizen: a. Minor age is less than 18. b. Adult age is greater than 18
#and less than 60 c. Senior citizen age is greater than 60

user_age=int(input("Enter age: "))
if user_age<18 and user_age>0:
    print("he is minor")
elif user_age>=18 and user_age<60:
    print("he is adult")
else:
    print("he is senior ciitzen")
