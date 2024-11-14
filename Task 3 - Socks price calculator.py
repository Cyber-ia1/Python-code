import time
import random # this is built in to create random situations


def socks_price_calculator():
    priceOfsocks = 100  

    while True:  # creates an infinite loop that allows user to restart
        random_number = random.randint(1, priceOfsocks) ## this line code will genarate the price of socks depending on limit set 

        print("welcome to socks price calculator, enter your budget\n")
        myWallet = int(input())  # user enters their budget

        print("\nYour budget for socks is", + myWallet)

        time.sleep(2)

        print("\nThe price of socks with todays infltion is", + random_number)

        time.sleep(3)

        print("\nCalculating...........\n[-----]\n| o o |\n|  ^  |\n| '-' |\n|_____|\n|     |\n|     |\n|_____|\n|_| |_|\n")
                                      

        time.sleep(7)

        if random_number <= myWallet:                        # basic for loop
           print("\nYou can finally keep your feet warm")
        else:
           print("\nYou are broke, no warm feet for you")

        time.sleep(2)

        Final = myWallet - random_number    # This line calculates the wallet after purchase 

        print("\nYour change will come to ", Final)     # this prints the user the total 
        
        time.sleep(3)

        restart = input("\nWould you like to try again?\nType (yes/no): ").strip().lower()

        if restart != "yes":
            print("\nGoodbye!")
            break  # This will exit the loop if the user does not want to continue

socks_price_calculator()  # runs the loop again
