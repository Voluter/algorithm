# -*- coding=utf-8 -*-
class LNode:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

'''
建立一个链表并且遍历

list1=LNode(1)
p=list1
for i in range(2,12):
    p.next=LNode(i)
    p=p.next
p=list1
while p is not None:
    print(p.elem)
    p=p.next

'''


