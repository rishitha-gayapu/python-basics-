'''#n=int(input("enter a number"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        print(i)
        count=count+1
print("count=",count)'''#
#effective way
n=int(input("enter a number"))
count=0
i=1
while(i<=(i/2)):
    if(n%i==0):
        if(i==(n/2)):
            count=count+1
        else:
            count+=2
    i=i+1
print("count=",count)
    
