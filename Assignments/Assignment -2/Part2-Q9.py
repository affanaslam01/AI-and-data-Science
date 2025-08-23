#Write a program that continues to ask user to input password until the correct password is entered.

while True:
    password=input("Enter a password: ")
    
    if password=="ahmed":
        print("password is correct")
        break
