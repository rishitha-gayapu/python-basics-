import random as r
n=r.randrange(1,50)
guess=int(input("guess the no"))
while n!=guess:
    if guess<n:
        print("too low")
        guess=int(input("guess the no"))
    elif guess>n:
        print("too high")
        guess=int(input("guess the no"))
    else:
        break
    print("you r right")
    
        
