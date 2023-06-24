v=int(input())
w=int(input())
if(w&1==1 or w<2 and w<=v):
    print("invalid")
else:
    x=((4*v)-w)//2
    print("tw={0},fw={1}",format(x,v,x))
    
