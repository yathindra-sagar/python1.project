import random
def rolldice(points):
    guess=random.randint(1,6)
    human=int(input("Enter a number between'1-6':- "))
    if(human==guess):
        print("You Won"+","+"You Scored:- 5 points")
        print("______Wanna play one more match____")
        choice=input("Yes or No:- ")
        if choice=="Y" or choice=="y" or choice=="Yes" or choice=="yes":
            rolldice(points+5)
        elif choice=="n" or choice=="N" or choice=="No" or choice=="no":
            z="Total points scored:-"
            w="Game over"
            print(z,points,w)
    elif(human not in [1,2,3,4,5,6]):
            #return "Wrong Input","Enter Again"
        print("Wrong Input , Enter Again")
        rolldice(points)
    else:
        print("Wrong Guess!")
        print("______Wanna play one more match____")
        choice=input("Yes or No:- ")
        if choice=="Y" or choice=="y" or choice=="Yes" or choice=="yes":
            rolldice(points)
        elif choice=="n" or choice=="N" or choice=="No" or choice=="no":
            z="Total points scored:-"
            w="Game over"
            print(z,points,w)

points=0
rolldice(points)           