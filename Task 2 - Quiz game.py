import time


print("Welcome to the car quiz\n")

time.sleep(5)   # 5 second pause before the game starts

print("This game will require you to chose one of the 3 choices \nYou have no time limit\nGoodluck\n")

time.sleep(10)  # 10 second pause before the game starts

questions = [
    "1. What is the purpose of a car's engine?\n A) To make the car look nice\n B) To convert fuel into power to move the car\n C) To play music\n",
    
    "2. What is the difference between an automatic and manual transmission?\n A) Automatic changes gears itself, manual requires the driver to change gears\n B) Manual cars have more wheels\n C) Automatic cars are faster than manual\n",
    
    "3. How often should I change my car's oil?\n A) Every 1,000 miles\n B) Every 5,000-7,500 miles\n C) Never\n",
    
    "4. What does the check engine light mean?\n A) Your car needs a wash\n B) There is a problem with the engine or emissions system\n C) The tires are low on air\n",
    
    "5. What is a hybrid car?\n A) A car that uses only gasoline\n B) A car that uses both gasoline and electricity\n C) A car that can drive itself\n",
    
    "6. Why do tires need to be inflated properly?\n A) To help the car go faster\n B) For better fuel efficiency, safety, and tire life\n C) To make the car look better\n",
    
    "7. What is the function of a car battery?\n A) It powers the car's lights, radio, and helps start the engine\n B) It powers the car's fuel system\n C) It makes the car faster\n",
    
    "8. What does MPG stand for?\n A) Miles Per Gallon\n B) Motor Performance Gauge\n C) Maximum Power Gear\n",
    
    "9. Why is regular car maintenance important?\n A) To keep the car shiny\n B) To keep the car running smoothly and prevent breakdowns\n C) To change the color of the car\n",
    
    "10. What should I do if my car overheats?\n A) Keep driving until you reach home\n B) Stop the car, turn off the engine, and wait for it to cool down\n C) Pour water over the engine\n"
]

answers = [
    "B",    #To convert fuel into power to move the car
    "A",    #Automatic changes gears itself, manual requires the driver to change gears
    "B",    #Every 5,000-7,500 miles
    "B",    #There is a problem with the engine or emissions system
    "B",    #A car that uses both gasoline and electricity
    "B",    #For better fuel efficiency, safety, and tire life
    "A",    #It powers the car's lights, radio, and helps start the engine
    "A",    #Miles Per Gallon
    "B",    #To keep the car running smoothly and prevent breakdowns
    "B",    #Stop the car, turn off the engine, and wait for it to cool down
]



# answers = [answer.strip().upper() for answer in input.split(",")]   #my first atempt at making the accepted answers case-insensitive

def quizGame(): ## This function will be called to every time the user asks a question, it also will keep track of the score
    score = 0
    for i in range(len(questions)):
       print(questions[i])
       ans = input("Please answer below: \n").strip().upper()  # Accept one answer from the user (case-insensitive).  # .strip() allows for spaces before or after answer to still return a correct.
       if ans == answers[i]:
          print("CORRECT!")
          score += 1
       else:
          print("Incorrect answer")
    
    print("\nDrum roll please.............\n") 
    
    time.sleep(1)

    print("Final score: ", + score)

quizGame()