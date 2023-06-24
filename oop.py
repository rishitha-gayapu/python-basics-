#general syntsx to create a class
#object_name=class_name()
'''class abc:
    var=10
    def display(self):
        print("this is in class method")
obj=abc()
print(obj.var)
obj.display()'''
#constructor class
class abc():
    def __init__(self,val):
        self.val=val
        print("the val is==",val)
obj=abc(1)
