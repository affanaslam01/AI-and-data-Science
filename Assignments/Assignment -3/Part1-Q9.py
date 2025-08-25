#Write a function to take user’s score as argument and determine if they pass or fail (pass if score is above 60, otherwise fails.)
def function(user_score):
    if user_score>60:
        return "pass"
    else:
        return "fail"
result=function(61)
print("Result:",result)
