l=[3,1,5,5,3,3,5,3,2,2]
for i in l:
    c=0
    for j in l:
        if(i==j):
            c+=1
    if(c==1):
        print(i)
        break
