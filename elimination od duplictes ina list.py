l=[8,5,8,3,1,5,3,1,9,9]
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if(l[i]==l[j]):
            count=count+1
        else:
            count=0
    if(count==1):
        print(l[i])
        break;
    continue;
pass;
    