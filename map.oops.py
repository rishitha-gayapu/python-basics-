def addition(n):
    return n+n
def mul(n):
    return n*n
num=(7,8,9,10,12)
result=map(addition,num)
result1=map(mul,num)
print(list(result))
print(list(result1))
