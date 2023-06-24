a=[-4,-2,1,3,7,9,10]
b=[-1,5,11]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if(l[j]>l[j+1]):
            x=a[j]
            a[j]=a[j+1]
            a[j+1]=x
            
        
