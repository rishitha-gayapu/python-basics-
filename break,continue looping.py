'''i=1
while i<=10:
    print(i,end=" ")
    if(i>5):
        break
    i=i+1
print("over")'''
for i in range(1,11):
    if(i==5):
        continue
    print(i,end=" ")
print("over")
