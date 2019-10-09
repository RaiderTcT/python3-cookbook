# @作者     ： Ulysses
# @功能描述 ： 在lambda中绑定变量的值
# @修改记录 ： 2019/2/14 16:27 创建

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10), b(10))  # x是自由变量， 在运行时绑定变量的值
# 30 30

funcs = [lambda x: x+n for n in range(5)]
print(funcs)  # 还没有执行
# [<function <listcomp>.<lambda> at 0x00000000029B1598>, <function <listcomp>.<lambda> at 0x00000000029B1620>, <function <listcomp>.<lambda> at 0x00000000029B16A8>, <function <listcomp>.<lambda> at 0x00000000029B1730>, <function <listcomp>.<lambda> at 0x00000000029B17B8>]
for f in funcs:
    print(f(0), end=' ')  # 4 4 4 4 4

print()
funcs_1 = [lambda x, n=n: x+n for n in range(5)]
for f in funcs_1:
    print(f(1), end=' ')  # 1 2 3 4 5
