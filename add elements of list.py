import functools
def add(x,y):
    return x+y
nums=[9,8,7,6,5]
print(functools.reduce(add,nums))
    
    
