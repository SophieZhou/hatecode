# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:08:17 2022

@author: Administrator
"""

"""
graph
"""
from collections import deque
graph={}
graph['you'] = ['alice','bob','clark']
graph['bob'] = ['andy','peggy']
graph['alice'] = []
graph['clark'] = []
graph['andy'] = []
graph['peggy'] =[]

def person_is_seller(name):
    return name[-1]=='y'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person,'is a mango seller')
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search('you')