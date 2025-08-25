#Write a function to take user’s age as argument and return the message from the function whether he is minor, adult or senior citizen:
#a.	Minor age is less than 18.
#b.	Adult age is greater than 18 and less than 60
#c.	Senior citizen age is greater than 60
def func(age):
    if age<18 and age>0:
        return "He is minor"
    elif age>18 and age<60:
        return "He is adult"
    elif age>60:
        return "He is senior citizen"
    else:
        return "invalid age"
users_age=func(61)
print(users_age)
