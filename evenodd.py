num=int(input("enter a no"))
if(num%2==0 and num>0):
    print("even positive")
elif(num%2==0 and num<0):
    print("even and negetive")
elif(num%2!=0 and num<0):
    print("odd negetive")
else:
    print("odd positive")
