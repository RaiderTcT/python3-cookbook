#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 延迟属性, 惰性求值
Desc : 
"""
import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):  # 只定义 一个__get__ 非数据描述符
        if instance is None:
            return self
        else:
            value = self.func(instance)
            # 以property相同的名字的方式保存计算出的值， 会保存在实例字典中, 并且先访问实例字典
            setattr(instance, self.func.__name__, value)
            return value


def lazyproperty2(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
            # 需要使用getattr函数处理, 比在实例字典中查找速度慢
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy

class Circle:
    def __init__(self, radius):
        self.radius = radius


    @LazyProperty  # property 就是一个轻量级的描述符
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

    @lazyproperty2
    def area2(self):
        print('Computing area 2')
        return math.pi * self.radius ** 2



c = Circle(5.0)
print(c.radius)
print(c.area)
# Computing area
# 78.53981633974483
print(c.area)
# 78.53981633974483
print(c.perimeter)
# Computing perimeter
# 31.41592653589793
print(c.perimeter)
# 31.41592653589793
print(vars(c))
# {'radius': 5.0, 'area': 78.53981633974483, 'perimeter': 31.41592653589793}
c.area = 25
print(c.area)  # area变为可变的 mutable

print(c.area2)
print(c.area2)
# Computing area 2
# 78.53981633974483
# 78.53981633974483
c.area2 = 111  # AttributeError: can't set attribute
