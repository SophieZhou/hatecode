# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:18:29 2022

@author: zhoujy
"""

class vehicle():
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
        
        
class taxi(vehicle): 
    def __init__(self,passengers=None):
        super().__init__() # super(bus,self).__init__()  # 2.7
        print('taxi')
    def pick(self,*name):
        if len(self.passengers)>0:
            print('The taxi is busy already.') 
        elif len(name)>4:
            print('Too many')
        else:
            self.passengers = list(name)

    def drop(self):
        self.passengers.clear()

class bus(vehicle):
    def __init__(self,passengers=None):
        super().__init__()
        print('bus')
    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)


t = taxi()
t.pick('emily','ross','lily','tom')
print(t.passengers)
t.drop()

t.pick('Guke')
print(t.passengers)
t.pick('guk2')


b = bus()
b.pick('1')
b.pick('2')
print(b.passengers)






    