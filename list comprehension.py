'''l1=[10,20,30]
l2=[30,40,50]
print([(i,j) for i in l1 for j in l2])'''
print([(x,y) for x in [10,20,30] for y in [30,40,50] if x!=y])

