#!/usr/bin/env python 
#-*-coding:utf-8-*-
from types import MethodType
import sys
import random
import re
import string
import time
from datetime import datetime
import requests
import json
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

def get_customer_online_state(business_ids):
    
    url = 'http://v1.platform.chat.hicao.com/cs/chat.cgi' 
    headers = { 
        'Cookie':'PHPSESSID=ed012b9vt17gg1986aod1l6et1',
    }   
    #str_business_ids = ','.join(business_ids)
    str_business_ids = '745,11,765,803,747'
    query = {}
    query["version"] = "2.0"
    query["message_type"] = 70
    query["business_id_list"] = str_business_ids
    print str_business_ids
    isOnline = 0 
    business_id2online_state = {business_id:isOnline for business_id in business_ids}
    res = requests.post(url,data="data:"+json.dumps(query),headers=headers,verify=True)
    print res
    result = res.json()
    if result.has_key("state_list"):
        state_list = result['state_list']
        for bid, current_platform in state_list.items():
            is_online_curr = 0 
            for item in current_platform['platform']:
                if item["state"] == 0:
                    is_online_curr = 1 
                    break
            business_id2online_state[str(bid)] = is_online_curr
    return business_id2online_state

if __name__=='__main__':
    business_ids = [745,11,765,803,74]
    get_customer_online_state(business_ids)
