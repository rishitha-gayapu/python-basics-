d={n:n*n for n in range(1,5)}
print(d)
#cal product price
old={'rice':50,'dal':100,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)
#with checks
real={'sam':25,'angel':19,'esha':21}
now={name:age for (name,age) in real.items() if age>20}
print(now)
