import time # imported time function to allow time for user to enter details

print("Welcome, to SuccessHub")
print("LOGIN")
print("Username:__________  Username must only contain lowercase letters and no spaces")

username = input()

time.sleep(2)

print("Password:_________  Password must only contain numbers and no spaces")

password = input()

time.sleep(2)

print("Username entered:", username)
print("Password entered:", password)

print("To create a account a with SuccessHub we must verify your age") 
print("Enter your age____")

age = int(input())

if age >= 18:
    print("Congratulations your account has been created, Success awaits")
else:
    print("You must be 18 or over to create an account with success hub") 