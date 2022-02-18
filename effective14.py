# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:04:53 2022

@author: Administrator
"""

''''
sort函数，比较容易用的是reverse，而其中还有个参数key，默认是NONE，
此时排序是按照默认比较方法排序，比如数据按照大小，字符串按照字符的顺序，
这种python中存在的数据类型，比较起来还是比较简单的。但是如果你比较的是objects，
比较复杂，不能再按照数据大小或者字符串顺序比较排序时，怎么办呢？你需要给你的比较
对象指定排序方法。比如两个人，怎么排序？比较年龄还是比较姓名进行排序？
这就是key发挥作用的时候了，此时通过key这个参数指定我们要做排序的objects，
是用什么方法来排序，按照人名还是年龄还是体重还是身高还是颜值呢？
因此key这个参数需要的是function,这个func完成排序的方法。
''''

# In[]
## Item 14: Sort by Complex Criteria Using `key` Parameter
"""
* Use `sort()` method to sort built-in types which has 
a natural ordering to them:

"""
numbers = [93, 46, 75, 33, 0, 23, 33]
numbers.sort()
print(numbers)
# In[]
"""
* `sort()` do not work directly on objects. 
You need to use `key` parameter, which accepts function:
"""
class Tool():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


tools = [
    Tool("level", 3.5),
    Tool("hammer", 1.25),
    Tool("screwdriver", 0.5),
    Tool("chisel", 0.25),
]

print("Unsorted:", repr(tools))
tools.sort(key=lambda x: x.name)  # ordered by x.name
print("\nSorted:", tools)

# In[]
"""
* For `str` you may want to lower case each item in a 
list to ensure that they are in alphabetical order
"""

places = ["home", "work", "New York", "Paris"]
places.sort()
print("Case sensitive:", places)
places.sort(key=lambda x: x.lower())
print("Case insensitive:", places)
# In[]
"""
* for sorting with multiple criteria you may use `key` parameter
 returning `tuple` containing two attributes in required order:
tuple 实现按照多个指标进行排序的目的，先按照第一个元素排序，然后第二个，
但是不管有多少个排序指标，排序的先后顺序(从小到大，从大到小等)都一样，因为reverse是作用在所有指标
上的。如果某一个元素是可否定(negation)，则可以在这个指标前加个-，实现顺序和reverse设定的是反过来的。
但是并不是所有元素都可以这么做，比如下面例题中，x.name字符串是没办法加-进行否定的。
此时就不可以这么做，但是x.weight可以，因为是数值，可以加-。此时如果你想按照两个指标
进行排序，那么不能再用tuple这种方式了，你可以把各个指标分开对objects进行
排序，先按照lowest的元素进行排序，再按照highest的元素进行排序。
"""
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)
"""
* Negation on `int`'s may be used to sort in different directions:
"""
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)
""""
* To combine mane sorting criteria and different directions 
combine `sort` function calls following way and use `reverse` 
for changing direction:

"""
power_tools.sort(key=lambda x: x.name)
power_tools.sort(key=lambda x: x.weight, reverse=True)
print(power_tools)

