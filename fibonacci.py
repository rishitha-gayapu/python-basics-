'''#def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  
n = int(input("How many terms? "))   
if n <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(n):
       print(fibo(i))'''
#
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
n=int(input("enter  a number"))
for n in range(0,n):
    print(fibo(n),end=" ")
