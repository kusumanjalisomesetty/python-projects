import random
print("welcome to number guessing game")
print("I am Damn sure this will be very interesting")
types=input("Press easy or Hard!!!! In case of Easy You will be having 10 attemts to guess otherwise 5 attempts")
if types=="easy" or types=="EASY":
    print("You are having 10 attempts to guess the number")
    print("You have to guess the number between 1 to 100")
    number=random.randint(1,100)
    guess=int(input())
    attempts=10
    answer=0
    while(attempts>0):
         if guess<number:
             print("Your Guess is too low")
             attempts=attempts-1
             print(f"You have left with {attempts} chances")
             guess = int(input())
         elif guess>number:
              print("Your Guess is too high")
              attempts=attempts-1
              print(f"You have left with {attempts} chances")
              guess = int(input())
         else:
              print("Congratulations!!! Your Guess is correct")
              print("Please give me rating for our Game out of 5")
              rating = int(input())
              print(f"thank you for giving {rating} rating")
              answer=1
              break
    if answer==0:
        print("Sorry you have lost Try again next time")
        print(f"The correct answer is {number}")
        print("Please give me rating for our Game out of 5")
        rating=int(input())
        print(f"thank you for giving {rating} rating")
        print("surely try again when you are free")
if types=="hard" or types=="HARD":
    print("You are having 5 attempts to guess the number")
    print("You have to guess the number between 1 to 100")
    number=random.randint(1,100)
    guess=int(input())
    attempts=5
    answer=0
    while(attempts>0):
         if guess<number:
             print("Your Guess is too low")
             attempts=attempts-1
             print(f"You have left with {attempts} chances")
             guess = int(input())
         elif guess>number:
              print("Your Guess is too high")
              attempts=attempts-1
              print(f"You have left with {attempts} chances")
              guess = int(input())
         else:
              print("Congratulations!!! Your Guess is correct")
              print("Please give me rating for our Game out of 5")
              rating = int(input())
              print(f"thank you for giving {rating} rating")
              answer=1
              break
    if answer==0:
        print("Sorry you have lost Try again next time")
        print(f"The correct answer is {number}")
        print("Please give me rating for our Game out of 5")
        rating=int(input())
        print(f"thank you for giving {rating} rating")
        print("surely try again when you are free")


