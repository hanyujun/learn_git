#! /usr/bin/env python
#-*-coding:utf-8-*-
from Queue import Queue
if __name__=='__main__':
    qe = Queue()
    print qe.empty()
    for i in range(20):
        qe.put(i)
    print qe.empty()
    while not qe.empty():
        print qe.get()
