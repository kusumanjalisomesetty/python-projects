import random
import logo_art_2
import list_high_low
import os
def maximum():
    global list4
    max = 0
    for i in range(0, 2):
        if(list4[i] > max):
            max = list4[i]
    return max
score=0
final_result=0
for i in range(0,100):
     print(logo_art_2.logo1)
     list=list_high_low.data
     user1=random.randint(0,(len(list)-1))
     list2=(list[user1])
     print(f"compare1: {list2['name']} ,{list2['description']},from {list2['country']}")
     print(logo_art_2.logo2)
     user2=random.randint(0,(len(list)-1))
     list3=list[user2]
     print(f"compare2: {list3['name']} ,{list3['description']},from {list3['country']}")
     output1=(list2['follower_count'])
     output2=(list3['follower_count'])
     global list4
     list4=[output1,output2]
     wanna_end=False
     while not wanna_end:
         #score=0
         guess=int(input("who has more followers 0 or 1"))
         output3=maximum()
         print(f" the maximum number of followers are {output3}")
         if(list4[guess]==output3):
             print("your guess is correct")
             score=score+1
             print(f"ur score is {score}")
             wanna_end=True
             #os.system('cls')
         else:
             print(f"you r wrong and your final score is {score}")
             wanna_end=True
             final_result=1
             break
     #os.system('cls')
     if(final_result==1):
         print("thanks for using this game please give us review")
         review=int(input("enter your rating 1 to 5 1 is bad and 5 is good"))
         print(f"rating for this game is {review}")
         break

#play_again=input("do you want to play again type yes or no")

   #if(play_again=='yes'):
      #os.system('cls')
      #game()
   #else:
      # print("thanks for playing game  please give your review")
       #review=input("rank our game from 1 to 5")














import random
import logo_art_2
import list_high_low
import os
def maximum():
    global list4
    max = 0
    for i in range(0, 2):
        if(list4[i] > max):
            max = list4[i]
    return max
score=0
final_result=0
for i in range(0,100):
     print(logo_art_2.logo1)
     list=list_high_low.data
     user1=random.randint(0,(len(list)-1))
     list2=(list[user1])
     print(f"compare1: {list2['name']} ,{list2['description']},from {list2['country']}")
     print(logo_art_2.logo2)
     user2=random.randint(0,(len(list)-1))
     list3=list[user2]
     print(f"compare2: {list3['name']} ,{list3['description']},from {list3['country']}")
     output1=(list2['follower_count'])
     output2=(list3['follower_count'])
     global list4
     list4=[output1,output2]
     wanna_end=False
     while not wanna_end:
         #score=0
         guess=int(input("who has more followers 0 or 1"))
         output3=maximum()
         print(f" the maximum number of followers are {output3}")
         if(list4[guess]==output3):
             print("your guess is correct")
             score=score+1
             print(f"ur score is {score}")
             wanna_end=True
             #os.system('cls')
         else:
             print(f"you r wrong and your final score is {score}")
             wanna_end=True
             final_result=1
             break
     #os.system('cls')
     if(final_result==1):
         print("thanks for using this game please give us review")
         review=int(input("enter your rating 1 to 5 1 is bad and 5 is good"))
         print(f"rating for this game is {review}")
         break

#play_again=input("do you want to play again type yes or no")

   #if(play_again=='yes'):
      #os.system('cls')
      #game()
   #else:
      # print("thanks for playing game  please give your review")
       #review=input("rank our game from 1 to 5")














