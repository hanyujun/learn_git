#! usr/bin/env python
#-*-coding:utf-8-*-
import cPickle
import json
from datetime import datetime
import sys
REDIS_CLEINTS = [1,2,3,4,5]
class Worker(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

def test_taglist_upadte():
    now = datetime.now()
def test_cPickle():
    l = [1, 3, 2, 5]
    d ={'stu1': 21, 'stu2':22}
    lp = cPickle.dumps(l)
    print lp
    lpl = cPickle.loads(lp) 
    print lpl
    dp = cPickle.dumps(d)
    print dp
    dpd = cPickle.loads(dp)
    print dpd
def use_generator():
    lists = [x * x for x in range(10)]
    generator = (x * x for x in range(10))
    print lists
    print generator
    for g in generator:
        print g

def get_redis_client():
    index = 0
    count = len(REDIS_CLEINTS)
    while True:
        yield REDIS_CLEINTS[index]
        index = index + 1
        if index == count:
            index = 0

def dbjhash22(hash_str):
    base = 5831
    for c in hash_str:
        base =((base << 5) + base) + ord(c)
    return base
random_num = get_redis_client().next

if __name__=='__main__':
    hash_str = 'api2:user:2829978'
    base = dbjhash22(hash_str)
    print base
    #index = 0
    #while index < 100:
        #client = random_num()
        #print client
        #index = index + 1
