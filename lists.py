l=[1,2,"s",3,5.2]
l.append(8)
print(l)
l.extend([9,3,21])
print(l)
l.insert(4,'siri')
print(l)
l.pop(2)
print(l)
l.remove(8)
print(l)
l.reverse()
print(l)
l.index(5.2)
print("index=",l.index(5.2))
l2=[5,4,5,5,78,23,90]
l2.sort()
print(l2)
l2.count(5)
print("count=",l2.count(5))
l3=l2.copy()
print(l3)
print("length=",len(l2))
l2.clear()
print(l2)



