#! /usr/bin/env python
#-*-coding:utf-8-*-

class Stack(object):
    def __init__(self, stack):
        self.stack = stack
    def is_empty(self):
        return True if len(self.stack) <= 0 else False
    def pop(self):
        return (self.stack).pop() if len(self.stack) > 0 else None
    def push(self,elem):
        (self.stack).append(elem)
if __name__=='__main__':
    stack = []
    sa = Stack(stack)
    print sa.is_empty()
    for i in range(1,20):
        sa.push(i)
    while not sa.is_empty():
        print sa.pop()
        
        
