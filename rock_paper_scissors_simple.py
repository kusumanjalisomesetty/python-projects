import random
print("Hi guys welcome to Rock Paper Scissors Game")
print("Really I am Damn sure You will be really excited while you u r playing this game")
user_choice=int(input("Enter  0 for Rock , 1 for Paper , 2 for scissors"))
computer_choice=random.randint(0,2)
print(f"Computer has selected {computer_choice}")
if computer_choice==user_choice:
    print("It's a draw")
elif computer_choice > user_choice:
    print("User has lost")
elif computer_choice < user_choice:
    print("User has won")
elif computer_choice==0 and user_choice==2:
    print("User has lost")
elif computer_choice==2 and user_choice==0:
    print("User has won")
else:
    print("Enter valid number")
