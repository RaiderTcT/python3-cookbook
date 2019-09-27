#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 分组迭代
Desc : 
itertools.groupby(iterable, key=None)
创建一个迭代器，返回 iterable 中连续的键和组。
key 是一个计算元素键值函数。
如果未指定或为 None，key 缺省为恒等函数（identity function），返回元素不变。
一般来说，iterable 需用同一个键值函数预先排序。
返回的组本身也是一个迭代器，它与 groupby() 共享底层的可迭代对象。
因为源是共享的，当 groupby() 对象向后迭代时，前一个组将消失。
因此如果稍后还需要返回结果，可保存为列表
"""
from operator import itemgetter
from itertools import groupby


def group_iter():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))
    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)

    # defaultdict使用
    from collections import defaultdict
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

if __name__ == '__main__':
    group_iter()
