#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @作者     ： Ulysses
# @功能描述 ： repr和str
# @修改记录 ： 2019/2/15 15:48 创建

class Pair:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):  # 满足obj==eval(repr(obj)), 不能完成时产生一段有意义的文本 < >
        # !r 使用__repr__()的输出而不是默认的__str__()
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
        # return 'Pair(%r, %r)' % (self.x, self.y)

    def __str__(self):  # 没有str 就会使用repr的结果
        # 将实例转为字符串，str() print()产生的结果
        return "({0.x!s}, {0.y!s})".format(self)

p = Pair(1, 2)
print(repr(p))
print(p)
# Pair(1, 2)
# (1, 2)
