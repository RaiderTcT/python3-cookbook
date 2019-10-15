# @作者     ： Ulysses
# @功能描述 ： 访问定义在闭包内的变量
# @修改记录 ： 2019/2/15 11:48 创建
import sys

def sample():
    n = 0

    def func():
        print('n =', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals =sys._getframe(1).f_locals  # 获取调用当前函数的函数的局部变量

        # ClosureInstance实例的方法 会被替换成 locals的可调用方法
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)
    print(sys._getframe().f_locals)  # 当前函数的局部便量
    # 将内层数据拷贝到一个实例字典中返回
    return ClosureInstance()

if __name__ == "__main__":

    f = sample()
    f()
    f.set_n(11)
    f()

    s = Stack()
    s.push(10)
    s.push(20)
    s.push('test')
    print(len(s))
    print(s.pop())
    print(s.pop())
