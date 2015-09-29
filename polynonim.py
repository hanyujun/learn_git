#!/usr/bin/env python 
#-*-coding:utf-8-*-
from types import MethodType
import sys
import random
import re
import string
import time
from datetime import datetime
TEL_REG = r"(13|14|15|17|18)\d{9}$"
class Animal(object):
 def run(self):
    print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')
class Cat(Animal):
    def run(self):
        print('Cat is running')
def test_run(animal):
    animal.run()
def set_age(self, age):
    self.age = age
def test_sys():
    sys.path.append('.')
    for sp in sys.path:
        print sp
def random_choice():
     count = 0
     while count <= 15:
        count += 1
        i = random.choice([0,0,0,0.8,0,0.6,0.8,0.5])
        print i
def test_use_reg(str_number):
    regx = TEL_REG
    p = re.compile(regx)
    if p.match(str(str_number)):
        return True
    else:
        return False
def test_time():
    now = time.localtime()
    if now.tm_hour <= 12: 
        hour = 14
    else:
        hour = 23
    publish_date = int(time.mktime(datetime(now.tm_year, now.tm_mon, now.tm_mday, hour, 0, 0).timetuple()))
    print publish_date
if __name__=='__main__':
    test_time()
