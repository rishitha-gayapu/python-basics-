class parent:
    def display(self):
        print("parent child")
#derived class
class child(parent):
    def show(self):
        print("child class")
c=child()
c.display()
c.show()
