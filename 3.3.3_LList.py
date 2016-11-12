class LNode:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

#基于节点LNode定义一个单链表对象的类
class LList:
    def __init__(self):
        self._head=None
    
    def is_empty(self):
        return self._head is None
    
    def prepend(self,elem):
        self._head=LNode(elem,self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e=self._head.elem
        self._head=self._head.next
        return e

    def append(self,elem):
        if self._head is None:
            sel._head=LNode(elem)
            return
        p=self._head
        while p.next is not None:
            p=p.next
        p.next=LNode(elem)
    
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p=self._head
        if p.next is None:
            e=p.elem
            self._head=None
            return e
        while p.next.next is not None:
            p=p.next
        e=p.next.elem
        p.next=None
        return e

    def find(self,pred):   #找到满足给定条件的链表元素
        p=self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p=p.next

    def printall(self):
        p=self._head
        while p is not None:
            print(p.elem,end=' ')
            if p.next is not None:
                print(', ',end=' ')
            p=p.next
        print('')

