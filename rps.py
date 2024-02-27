# Rock Paper Scissors Game
from random import randint
l=["Rock","Paper","Scissor"]
print("Welcome to Rock Paper Scissors Game")
x=True
while x:
    p=input("enter your choice from Rock,Paper,Scissor: ")
    c=l[randint(0,2)]
    if p in l:
        print("Computers Choice is ",c)
    if p==c:
        print("TIE!")
    elif p=="Rock":
        if c=="Scissor":
            print("You WIN!,",p,"smashes",c)
        else:
            print("You LOSE!,",c,"covers",p)
    elif p=="Paper":
        if c=="Rock":
            print("You WIN!,",p,"covers",c)
        else:
            print("You LOSE!,",c,"cuts",p)
    elif p=="Scissor":
        if c=="Paper":
            print("You WIN!,",p,"cuts",c)
        else:
            print("You LOSE!,",c,"smashes",p)      
    else:
        print("Invalid Choice")
        x=False
              
