class Node:
    def __init__(self,n1,ar1,va1,n2):
        self.name=n1
        self.aVar=ar1
        self.var1=va1
        self.next=n2
    def __init__(self,n1,ar1,va1):
        self.name=n1
        self.aVar=ar1
        self.var=va1
        self.next=0
class Queue:
    def __init__(self):
        self.head=self.tail=0
    def addAtTail(self,v,n,n1):
        if self.head==0:
            self.head=self.tail=Node(v,n,n1)
        else:
            a=Node(v,n,n1)
            self.tail.next=a
            self.tail=self.tail.next
    def removeFromHead(self):
        if self.head==0:
            return False
        self.head=self.head.next
        return True
    def printQueue(self):
        variable=self.head
        while variable!=0:
            print(variable.aVar)
            variable=variable.next
    def empty(self):
        if self.head==0:
            return True
    def delNode(self,v):
        if self.head!=0:
            variable=self.head
            if variable.name==v:
                self.head=self.head.next
            else:
                while variable.next!=0:
                    if variable.next.name==v:
                        variable.next=variable.next.next
                        break
                    variable=variable.next
    def getName(self):
        return self.head.name
    def getAValue(self):
        return self.head.aVar
    def getValue(self):
        return self.head.var
    def getEarliest(self):
        v=self.head
        node=self.head
        while True:
            if node==0:
                return v
            if int(node.aVar)<int(v.aVar):
                v=node
            node=node.next
file=open("File1.txt","r")
c1=Queue()
for element in file:
    data=element.split()
    print(data)
    c1.addAtTail(data[0],data[1],data[2])
c1.printQueue()
print('|')
value=0
while c1.empty()!=True:
    node=c1.getEarliest()
    a=node.name
    print(a)
    b=int(node.aVar)
    while value<b:
        print('.')
        value+=1
    c1.printQueue()
print(value)