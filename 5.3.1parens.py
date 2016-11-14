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
            return None
        p=self._top
        self._top=self._top.next
        return p.elem

#检查匹配问题


def check_parens(text):
    parens="()[]{}"
    open_parens="([{"
    opposite={")":"(","]":"[","}":"{"}

    def parenthese(text):
        i,text_len=0,len(text)
        while True:
            while i<text_len and text[i] not in parens:
                i+=1
            if i>=text_len:
                return
            yield text[i],i
            i+=1
    st=LStack()
    for pr,i in parenthese(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop()!=opposite[pr]:
            print("Unmatching is found at",i,"for",pr)
            return False
    print("All parens are correctly match!")
    return True

#检查匹配问题
text="IPIPOIPIPO{{}(((())))JK())[io][ppp]]"
f=check_parens(text)
#输出  Unmatching is found at 25 for )

