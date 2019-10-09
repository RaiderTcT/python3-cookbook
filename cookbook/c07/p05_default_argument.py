#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 函数默认参数
Desc : 
"""

def spam(a, b=42):
    print(a, b)

spam(1) # Ok. a=1, b=42
spam(1, 2) # Ok. a=1, b=2

# 默认值是可变容器（列表、集合或字典），使用None作为默认值
def spam_1(a, b=None):
    if b is None:
        b = []

_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

x = 23

def spam_3(a, b=x):  # 对默认参数的赋值只会在函数定义时绑定一次
    print(a, b)

spam_3(1)  # 1 23
x = 44
spam_3(34)  # 34 23
