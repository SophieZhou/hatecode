# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 09:36:16 2022

@author: Administrator
"""

# In[]
'''
global  
nonlocal
#local
'''
x=10
def fun():
    print(x)
    
fun()
# In[]
'''
result:
10000
10
here x is a local variable, it is visible just in the function of fun(). It 
has no relationship with the x variable outside.
'''
x=10
def fun():
    x=10000
    print(x)
    
fun() 
print(x)



# In[]
'''
result:
UnboundLocalError: local variable 'x' referenced before assignment

you can do assignment to the variable x, and it will be a local variable.
here the sentence 'x=x+1' is assignment but the x has not initialization.  
'''


x=10
def fun():
    x=x+1
    print(x)
    
fun()    

# In[]
'''
if you do this, there will be non error anymore. But the x is a variable just
visible in the function fun().
'''
x=10
def fun():
    x=0
    x=x+1
    print(x)
    
fun() 
print(x)   


# In[]
'''
Used the keyword global to announce that the x is global, it is the one outside.
Here you can use x in the function fun() as outside.

'''
x=10
def fun():
    global x 
    x=x+1
    print(x)
    
fun()    
print(x)

# In[]
'''
nonlocal
in closure, when the function inside want to visit esp change the parameter outside,
you should use nonlocal to solove.
'''


def fun(x):
    def inner(y):
        print(x+y)
    return inner
    
f = fun(10)  
f(1)

# In[]
'''
You can not do assignment with the parameter x above. 
But you can do this below.And it is not the same with global because
the variable x outside do not change. The change just appear in the function.
'''
x=10
def fun(a):
    global x
    x = 2
    def inner(y):
        global x
        nonlocal a        
        a=a + 10
        x=a + y
        print(x)
    return inner
    
f = fun(10) 
f(1)
print(x)

# In[]
'''
But nonlocal appears in python 3.5 later. Without nonlocal you can only use
list or dict, these variables is not like integer or str which can not vary.
Here you are not doing assignment actually.
'''
def fun(lst):
    def inner(y):
        lst.append(y)
        print(len(lst))
    return inner
lst = []
f = fun(lst)  
f(1)
f(2)
f(3)
f(4)


# In[]
def fun():
    lst = []
    def inner(y):
        lst.append(y)
        print(len(lst))
    return inner

f = fun()  
f(1)
f(2)
f(3)
f(4)



# In[]
'''
'''
