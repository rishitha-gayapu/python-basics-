class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            print(temp.data,end="-->")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,end="-->")
            print(temp.next.data)
    def detect_loop(self):
        if self.tail.next==self.head:
            print("loop exists")
            
C=CLL()
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
C.head=n1
C.tail=n1
C.tail.next=C.head
n1.next=n2
C.tail=n2
C.tail.next=C.head
n2.next=n3
C.tail=n3
C.tail.next=C.head
n3.next=n4
C.tail=n4
C.tail.next=C.head
C.display()
C.detect_loop()
C.display()
