#-*- coding:utf-8 -*-
#栈的链接表实现
class LNode:
    def __init__(self,elem, next_):
        self.elem=elem
        self.next=next_

class StackUnderflow(ValueError):
    pass

class LStack():
    def __init__(self):
        self._top=None
    def is_empty(self):
        return self._top is None
    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem
    def push(self,elem):
        self._top=LNode(elem,self._top)
    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        p=self._top
        self._top=self._top.next
        return p.elem

#应用
st1=LStack()
for i in range(9):
    st1.push(i)
while not st1.is_empty():
    print(st1.pop(),end=" ")
