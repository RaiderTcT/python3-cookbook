#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 只允许关键字形式的参数
Desc : 
"""
# *开头的参数只能是作为 最后一个位置参数, **开头的参数只能作为最后一个参数出现
# 在*agrs之后的参数称为keyword-only参数， 既只能作为关键字参数出现
def a(x, *args, y):  # *args 解开后的元组
    print(args)  # 元组

a(1, 2, 3, 4, 5, y=5)   # args = (2, 3, 4, 5)
a(1, *(2, 3, 4, 5), y=3)  # args = (2, 3, 4, 5)
a(1, (1, 2, 3), y =3)  # args= ((1, 2, 3), )

def recv(maxsize, *, block):
    'Receives a message'
    pass

# recv(1024, True) # TypeError
recv(1024, block=True)  # Ok


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


minimum(1, 5, 2, -5, 10)  # Returns -5
minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0
