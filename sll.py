class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_at_strt(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def insert_at_end(self,data):
        newb=Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newb
        newb.next=None
    def insert_at_mid(self,pos,data):
        np=Node(data)
        temp=self.head
        while temp.data!=pos:
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def del_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:    #indicates that temp has some value 
                if temp.next!=None:
                    print(temp.data,end="->")
                else:
                    print(temp.data,end="")
                    print()
                temp=temp.next
        
obj1=singlelinkedlist()
n=Node(10)
obj1.head=n
n1=Node(20)
obj1.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
obj1.display()
obj1.insert_at_strt(5)
obj1.display()
obj1.insert_at_end(50)
obj1.display()
obj1.insert_at_mid(1,60)
obj1.display()
