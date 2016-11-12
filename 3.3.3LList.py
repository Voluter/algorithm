#-*-coding:utf-8 -*-
class LNode:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

class LList:
    def __init__(self):
        self._head=None

    def is_empty(self):
        return self._head is None
    
    def prepend(self,elem):
        self._head=LNode(elem,self._head)

    def append(self,elem):
        if self._head is None:
            self._head=LNode(elem)
            return
        p=self._head
        while p.next is not None:
            p=p.next
        p.next=LNode(elem)

    def pop_last():
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p=self._head
        if p.next is None:
            e=p.elem
            self._head=None
            return e
        while p.next.next is not None:
            p=p.next
        elem=p.next.elem
        p.next=None
        return elem
    
    def printall():
        p=self._head
        while p is not None:
            print(p.elem,end=' ')
            if p.next is not None:
                print(', ',end='')
            p=p.next
        print('')
    
    def for_each(self,proc):
        p=self._head
        while p is not None:
            proc(p.elem)
            p=p.next
            
    


