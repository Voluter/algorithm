class LNode:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

class LCList:
    def __init__(self):
        self._rear=None
    
    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):
        p=LNode(elem)
        if self._rear is None:
            p.next=p
            self._rear=p
        else:
            p.next=self._rear.next
            self._rear.next=p
            
    def append(self,elem):
        self.prepend(elem)
        self._rear=self._rear.next
    #弹出队首元素
    def pop(self):
        if self._rear is None:
            return "This is an empty list!"
        p=self._rear.next
        if p.next is p:
            self._rear=None
        else:
            self._rear.next=p.next
        return p.elem

    def pop_last(self):
        if self._rear is None:
            return "This is an empty list!"
        p=self._rear
        e=p.elem
        if p.next is p:
            self._rear=None
        else:
            while p.next is not self._rear:
                p=p.next
            e=self._rear.elem
            self._rear=p
        return e
        
             
    
    def printall(self):
        if self.is_empty():
            return
        p=self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p=p.next





mlist=LCList()
for i in range(10):
    mlist.prepend(i)
mlist.printall()
               
