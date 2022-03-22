# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:57:49 2022

@author: Administrator
"""


# In[]
# list 生成一个新的引用对象，只是用alst完成初始化
alst = [1,2,3,4,5]
blst=list(alst)
alst.append(6)
print(blst)

# In[]
alst = [1,2,3,4,5]
blst=alst # 浅拷贝，两者同时变化
alst.append(6)
print(blst)

# In[]
from  copy import copy

alst = [1,2,3,4,5]
blst=alst.copy() # 浅拷贝，两者同时变化
alst.append(6)
print(blst)

# In[]
import  copy 
alst = [1,2,3,4,5]
blst=copy.deepcopy(alst) # 深拷贝，可以认为是用alst初始化一个新的对象
alst.append(6)
print(blst)


# In[]


# In[]

"""
>>> import copy
>>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
>>> bus2 = copy.copy(bus1)
>>> bus3 = copy.deepcopy(bus1)
>>> bus1.drop('Bill')
>>> bus2.passengers
['Alice', 'Claire', 'David']
>>> bus3.passengers
['Alice', 'Bill', 'Claire', 'David']

"""
'''
the default value of paramter is None
'''
import copy
# tag::BUS_CLASS[]
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
# end::BUS_CLASS[]

bus1 = Bus(['a','b','c'])
bus2 = copy.copy(bus1)
bus1.pick('d')
bus1.drop('a')
print(bus2.passengers)
bus3= copy.deepcopy(bus1)
print(bus3.passengers)
bus1.pick('a')
bus1.drop('d')
print(bus3.passengers)
print(bus1.passengers)



# In[]
'''
Mutable Types as Parameter Defaults:Bad Idea
'''


# tag::HAUNTED_BUS_CLASS[]
class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):  # <1>
        # should be list function to initialization the attribute
        self.passengers = list(passengers)  # <2>

    def pick(self, name):
        self.passengers.append(name)  # <3>

    def drop(self, name):
        self.passengers.remove(name)
# end::HAUNTED_BUS_CLASS[]

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HauntedBus()
print('bus2.passengers:',bus2.passengers)
bus2.pick('Carrie')
print('bus2.passengers:',bus2.passengers)

bus3 = HauntedBus()
print('bus3.passengers:',bus3.passengers)
bus3.pick('Dave')
print('bus3.passengers:',bus3.passengers)
print(bus2.passengers is bus3.passengers)
print('bus2.passengers:',bus2.passengers)



# In[]
'''
here the attribute passengers should be initialized using a list func.

'''

# tag::TWILIGHT_BUS_CLASS[]
class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # <1>
        else:
            # this can change the passengers when you change self.passengers
            self.passengers = passengers  #<2> 

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # <3>
# end::TWILIGHT_BUS_CLASS[]

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)