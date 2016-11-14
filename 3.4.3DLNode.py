class LNode:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_
        
class DLNode(LNode):
    def __init__(self,elem,next_=None,pre=None):
        LNode.__init__(self,elem,next_)
        self.pre=pre

class DLList:
    def __init__(self):
        self._rear=None
        self._head=None
    
    def prepend(self,elem):
        if self._head is None and self._rear is None:
            self._rear=DLNode(elem)
            self._head=self._rear
        else:
            if self._rear is self._head:
                self._head=DLNode(elem,self._rear,None)
                self._rear.pre=self._head
            else:
                self._head=DLNode(elem,self._head,None)

    def append(self,elem):
        if self._head is None and self._rear is None:
            self._rear=DLNode(elem)
            self._head=self._rear
        else:
            if self._rear is self._head:
                self._rear=DLNode(elem,None,self._head)
                self._head.next=self._rear
            else:
                self._rear=DLNode(elem,None,self._rear)

    def pop_last(self):
        if self._head is None and self._rear is None:
            return "This is an empty list!"
        if self._head is self._rear:
            p=self._rear
            self._rear=None
            self._head=None
        else:
            p=self._rear
            self._rear=self._rear.pre
            self._rear.next=None
        return p.elem
            

    

    def printall(self):
        if self._head is None and self._rear is None:
            return
        p=self._head
        while p is not None:
            print(p.elem,end=" ")
            p=p.next
        




#测试双向链表
mlist=DLList()
#将3，4，5添加到末尾


#将6到10添加到队列的开头
for i in range(6,14):
    mlist.prepend(i)
for i in range(6,10):
    mlist.prepend(i)

mlist.printall()

#弹出队尾元素



        
