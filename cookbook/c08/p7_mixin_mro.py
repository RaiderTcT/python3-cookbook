# @作者     ： Ulysses
# @功能描述 ： 类多重继承顺序
# @修改记录 ： 2019/2/21 11:27 创建
"""
A    B
|    |
C    D
 \  /
   E
E C A D B

   X
  / \
 Y   Z
  \ /
   Temp
Temp  Y Z X
"""


class A:
    article = 'a'
    def spam(self):
        print('A.spam')

class B:
    article = 'b'
    def spam(self):
        print('B.spam')

class C(A):
    article = 'c'
    def spam(self):
        print('C.spam')

class D(B):
    article = 'd'
    def spam(self):
        print('D.spam')

class E(C, D):
    def spam(self):
        print('E.spam')
        super(C, self).spam()

e = E()
print(E.__mro__)  # E C A D B
e.spam()
# E.spam
# A.spam
print(e.article)
print('*'*20)
super(E, e).spam()
super(E, E).spam(e)
print('*'*20)
print(super(A, E).article)  # d
print(super(A, e).article)
class X:
    pass

class Y(X):
    pass

class Z(X):
    pass

class Temp(Y, Z):
    pass

temp = Temp()
print(Temp.__mro__)  # Temp Y Z X
