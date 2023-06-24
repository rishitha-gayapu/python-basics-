fact=1
i=1
n=int(input("enter a number"))
if(n==0):
    print("factorial of 0 is 1")
elif(n<0):
    print("we cant find fact for negetive numbers")
elif(n>0):
    for i in range(1,n+1):
        fact=fact*i
print("factorial of given no.is",fact)
