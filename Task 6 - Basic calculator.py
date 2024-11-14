# first step is to define the functions that the user will be able to complete

def add (x,y):   # addition
    return x + y

def sub (x,y):   # subtraction
    return x - y

def multiply (x,y):  # multiplication
    return x * y

def divide (x, y):   # division
    if y != 0:
        return x / y
    else:
        return "error, you cant divide by 0"


def Calculator():
    while True:   # starts the loop, to allow user to repeat the calculator function

     print("\nSelect an operation")
     print("1. Addition")
     print("2. Subtraction")
     print("3. Multiplication")
     print("4. Division")

     choice = input("\nEnter your choice \n[1]\n[2]\n[3]\n[4]\n")
    
     if choice in ['1', '2', '3', '4']:
        
         num1 = float(input("\nEnter first number: "))#.strip().upper()    # float is use in this, so the users input is recognised as an arithmatic.
         num2 = float(input("Enter second number: "))#.strip().upper()

     if choice == "1":
         print(f"\nThe result is: {add(num1, num2)}")
     elif choice == '2':
         print(f"\nThe result is: {sub(num1, num2)}")
     elif choice == '3':
         print(f"\nThe result is: {multiply(num1, num2)}")
     elif choice == '4':
         print(f"\nThe result is: {divide(num1, num2)}")
     else:
        
         print("\nInvalid Input! Please choose a valid operation.")

    
     again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
     if again != "yes":
         print("\nThank you for using the calculator. Goodbye!")
         break  # Exit the loop if the user says "no"



Calculator()
