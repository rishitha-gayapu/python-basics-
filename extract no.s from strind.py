s="hey253hii"
for i in s:
    if not((i>="a" or i>="A")and (i<="z" or i<="Z")):
        print(i)
name=input("enter a string")
for i in name:
    if(i.isdigit()==True):
        print(i,end="")

