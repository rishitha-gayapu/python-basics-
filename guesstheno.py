import random as r
x=r.randrange(1,50)
i=1
num=int(input("enter the no.in ur mind"))
while i<=50:
    guess=int(input("guess the no"))
    if guess<num:
        print("too low")
    elif guess>num:
        print("too high")
    else:
        print("you r right")
        break

