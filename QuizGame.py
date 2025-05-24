import art
print("Hi Guys welcome to sample quiz game :)")
print("I am Damn sure you will be really excited while playing the game!!!!")
play_or_not=input("Type yes/YES if You want to play otherwise type NO/no")
ques={
    0:"what is the capital of Australia? 1.Sydney 2.Canberra 3.Melbourne 4.Brisbane",
    1:"Who wrote the play Romeo and Juliet? 1.Charles Dickens 2.William Shakespeare 3.Jane Austen 4. George Orwell",
    2:"Which planet is known as the Red Planet? 1. Earth 2.Mars  3. Venus 4. Jupiter",
    3:"In which year did World War II end? 1.1940 2.1943 3.1945 4.1950",
    4:"Which element has the chemical symbol ‘O’? 1.Gold 2.Oxygen 3.Osmium 4.Ozone",
    5:"Who painted the Mona Lisa? 1.Pablo Picasso 2.Vincent van Gogh 3.Leonardo da Vinci  4.Michelangelo",
    6:"What is the longest river in the world? 1.Amazon River 2.Nile River 3.Yangtze River 4.Mississippi River",
    7:"What is the smallest prime number? 1)0 2)1 3)2 4)3 ",
    8:"Who is known as the father of computers?1.Alan Turing 2.Charles Babbage  3.Bill Gates 4.Steve Jobs",
    9:"Which country is famous for the Eiffel Tower? 1.Italy 2.Germany 3.Spain 4.France"
}
options=[2,2,2,3,2,3,2,3,2,4]
score=0
if play_or_not=="yes" or play_or_not=="YES":
    print(art.wel)
    print("Here Your Quiz starts")
    print("Hint:You have to enter the options either 1,2,3,4")
    print("!!!!!NOTE:There will be no negative marking for the wrong options")
    print("Hope You enjoy the game!!!!!!!")
    for i in range(10):
        print(ques[i])
        a=int(input("please enter your answer"))
        if(a==options[i]):
            score=score+1
            print(f"your score is {score}")
        else:
            print("sorry better luck next time")
            print(f"The correct option is {options[i]}")
    print(f"Your Final score is {score}")
    print("Thank You")
else:
    print("okay! No problem!!!!")
    print("Try it when you free on Some other Time!!!!!")
