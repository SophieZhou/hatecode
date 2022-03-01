# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:38:52 2022

@author: Administrator
"""
# In[]    
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count,total
        count += 1
        total += new_value
        return total/count 
    return averager   # 返回的是函数，带括号返回的函数运行结果
        
avg = make_averager()  # an object of function make_averager
print(avg.__name__) # the name is averager
avg(10)
avg(11)
res = avg(13)
res = avg(14)
print(res)

# In[]
def f(n):
    return n**2
    
def make_averager(func):
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count,total
        count += 1        
        res = func(new_value)
        print(count)
        total += res
        return total/count 
    return averager   # 返回的是函数，带括号返回的函数运行结果
        
avg = make_averager(f)  # an object of function make_averager
print(avg.__name__) # the name is averager
avg(1)
avg(2)
res = avg(3)
res = avg(4)
print(res)


# In[]
'''
虽然这么用不太好，但是也算是可以的。所以装饰器和闭包之间是什么关系呢？
有没有一目了然呢？
'''
    
def make_averager(func):
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count,total
        count += 1            
        res = func(new_value)
        total += res
        return total/count 
    return averager   # 返回的是函数，带括号返回的函数运行结果
        
@make_averager
def f(n):
    return n**2

'''
the decorator can be detailed below:
def f(n):
    return n**2
avg = make_averager(f)  # an object of function make_averager

'''
print(f.__name__)
f(10)
f(20)
# In[]
'''
closure
the free vairable is func
here the inner function clocked() can call func and  
'''

import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))        
        arg_str = ', '.join(arg_lst)
        print(arg_str)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked


'''
decorator
'''
@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
'''
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
factorial = clock(factorial)
'''

if __name__ == '__main__':
    print('*' * 20, 'Calling factorial(6)')
    print('6! =', factorial(6))


# In[]
# In[]
'''
closure
the free vairable is func
here the inner function clocked() can call func and  
'''

import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))        
        arg_str = ', '.join(arg_lst)
        print(arg_str)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked


'''
decorator
'''
#@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
'''
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
factorial = clock(factorial)
'''

if __name__ == '__main__':
   # print('*' * 20, 'Calling factorial(6)')
    print('6! =', factorial(6))   # 6! = 720
    
    
# In[]
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)    
    
    


# In[]
import time
def func_odd(num):
    for i in range(1,num+1):
        if num%2 ==1:
            print(num)

def func_time(func):
    t0 = time.perf_counter()
    func(100)
    t1 = time.perf_counter()
    print(t1-t0)
    
func_time(func_odd)


# In[]

from functools import wraps
import logging

def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL)
def plus(x, y):
    return x * y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam log test!')

spam()


add(3,4)

plus(3,4)
