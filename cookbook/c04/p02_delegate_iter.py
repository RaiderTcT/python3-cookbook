#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 代理迭代
Desc : 
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):  # iterable Node类实例变为可迭代对象
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # print(next(root))  TypeError: 'Node' object is not an iterator
    iter1 = iter(root)
    print(next(iter1))
    # Node(1)
    for ch in root:
        print(ch)
# Node(1)
# Node(2)
