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
    def insert_at_beg(self,data):
        nb=Node(data)
        temp=self.head
        if temp.next is None:
            self.head=nb
            self.tail=nb
            self.tail.next=self.head    
        else:
            while temp.next!=self.head:
                temp=temp.next
            nb.next=self.head
            self.head=nb
            self.tail.next=self.head
    def insert_at_end(self,data):
        ne=Node(50)
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=ne
        self.tail=ne
        self.tail.next=self.head
    def insert_at_mid(self,pos,data):
        np=Node(data)
        if self.head is None:
            temp=self.head
            self.tail=np
            self.tail.next=self.head
        else:
            if pos==1:
                insert_at_beg(data)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                np.next=temp.next
                temp.next=np
    def loop_exits(self):
        if self.head is not None:
            print("loop exists")
        else:
            print("no circular linked list")
    def del_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.tail.next=self.head
    def del_at_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next!=self.head:
            temp=temp.next
            prev=prev.next
        temp.next=None
        self.tail=prev
        self.tail.next=self.head
    def del_at_mid(self,pos,data):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def len(self):
        temp=self.head
        if self.head is None:
            return 0
        count=0
        if self.head!=None:
            while True:
                temp=temp.next
                count+=1
                if temp==self.head:
                    break
        return count
C=CLL()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
C.head=n1
C.tail=n1
C.tail.next=C.head
print(C.tail.next)
print(n1)
n1.next=n2
C.tail=n2
C.tail.next=C.head
print(C.tail.next)
print(n1)
n2.next=n3
C.tail=n3
C.tail.next=C.head
print(C.tail.next)
print(n1)
n3.next=n4
C.tail=n4
C.tail.next=C.head
print(C.tail.next)
print(n1)
C.display()
C.insert_at_beg(5)
C.display()
C.insert_at_end(50)
C.display()
C.insert_at_mid(3,70)
C.display()
C.del_at_beg()
C.display()
C.del_at_end()
C.display()
C.del_at_mid(2,80)
C.display()
print(C.len())
C.loop_exits()
