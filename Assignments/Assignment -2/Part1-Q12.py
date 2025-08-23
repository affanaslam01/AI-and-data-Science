#Write a program that takes a temperature in Celsius and checks if it is freezing, moderate or hot.
#a. Freezing temperature is below 0. b. Moderate temperature is greater than 0 and less than 26. c. Hot temperature is above 26.
temp=int(input("Enter temperature in Celsius: "))
if temp<0:
    print("Freezing Temperature")
elif temp>0 and temp<26:
    print("Moderate Temperature")
elif temp>26:
    print("Hot Temperature")
else:
    print("Exactly 0'celsius not to hot nor moderate")
