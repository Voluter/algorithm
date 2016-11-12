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
        p=LNode(elem)
        if self._rear is None:
            p=p.next
            self._rear=p
        else:
            p.next=self._rear.next
            p=self._rear

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p=self._rear
        if p.next==p:
            self._rear=None
            return p
        while p.next.next!=self._rear:
            p=p.next
        e=self._rear.elem
        p.next=self._rear.next
        self._rear=p
        return e

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p=self._rear.next
        if p.next==p:
            self._rear=None
        else:
            self._rear.next=p.next
        return p.elem
    
    def printall(self):
        if self._rear is None:
            return
        p=self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p=p.next

#循环单链表演示代码
mlist=LCList()
for i in range(10):
    mlist.append(i)
mlist.printall()
            
        







