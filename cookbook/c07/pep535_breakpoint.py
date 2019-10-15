# -*- coding: utf-8 -*-
# @作者     ： Ulysses
# @功能描述 ： python 内置断点
# @创建时间 ： 2019/4/4 9:21
"""
此函数会在调用时将你陷入调试器中。具体来说，它调用 sys.breakpointhook() ，
直接传递 args 和 kws 。默认情况下， sys.breakpointhook() 调用 pdb.set_trace()
且没有参数。在这种情况下，它纯粹是一个便利函数，因此您不必显式导入 pdb
且键入尽可能少的代码即可进入调试器。但是， sys.breakpointhook()
可以设置为其他一些函数并被 breakpoint() 自动调用，以允许进入你想用的调试器。
continue 或 c	继续执行程序
list 或 l	查看当前行的代码段
step 或 s	进入函数
return 或 r	执行代码直到从当前函数返回
exit 或 q	中止并退出
next 或 n	执行下一行
pp	        打印变量的值
help	    帮助
"""
a = "aaa"
breakpoint()
b = "bbb"
c = "ccc"
final = a + b + c
print(final)
