#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 通过描述器定义新的实例属性
Desc : 
"""

"""
描述符就是以特殊方法 __get()__, __set()__, __delete()__的形式实现了3个核心
的属性访问操作（get, set, delete）的类, 轻量级描述符协议
使用类名调用描述器，返回描述器本身
使用实例名调用描述器，返回自定义的值
"""
# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name  # Integer类实例的所有者类(Point)中的类变量名

    def __set__(self, instance, value):  # Integer类实例的所有者类的实例（p）
        if not isinstance(value, int):
            raise TypeError("需要输入int型")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):  # owner 所有者类 Point， instance 用来访问属性的实例p
        if instance is None:  # 通过类调用
            return self  # 标准做法, 不传入instance返回function本身
        else:
            return instance.__dict__[self.name]  # 返回一个bound method

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')  # 把描述符的实例放置在类的定义中作为类变量来使用
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.__dict__)
print(p.x, p.y)
print(Point.x)  # <__main__.Integer object at
# p.x = 2.5  # TypeError: 需要输入int型


# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

