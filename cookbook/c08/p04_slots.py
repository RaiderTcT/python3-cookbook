#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @作者     ： Ulysses
# @功能描述 ： 使用slots减少对内存的使用
# @修改记录 ： 2019/2/20 9:14 创建
import sys
from memory_profiler  import profile


class Date:
    __slots__ = ['year', 'month', 'day']  # 显式地声明数据成员（例如特征属性）并禁止创建 __dict__
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class Date_1:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

@profile
def date():
    d = [Date('2019', '02', '20') for _ in range(100000)]

@profile
def date_1():
    d = [Date_1('2019', '02', '20') for _ in range(100000)]


if __name__ == "__main__":
    date()
    date_1()
    d1 = Date('2019', '02', '20')
    d2 = Date_1('2019', '02', '20')
    # print(d1.__dict__)  #　has no attribute '__dict__'
    print(d2.__dict__)

"""
Line #    Mem usage    Increment   Line Contents
================================================
    21     16.1 MiB     16.1 MiB   @profile
    22                             def date():
    23     23.1 MiB      0.3 MiB       d = [Date('2019', '02', '20') for _ in range(100000)]

Line #    Mem usage    Increment   Line Contents
================================================
    25     17.2 MiB     17.2 MiB   @profile
    26                             def date_1():
    27     33.1 MiB      0.0 MiB       d = [Date_1('2019', '02', '20') for _ in range(100000)]
"""
