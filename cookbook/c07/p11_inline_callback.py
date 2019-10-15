# @作者     ： Ulysses
# @功能描述 ： 内联回调函数, 省去函数调用的开销（小型函数的泛滥）
# @修改记录 ： 2019/2/15 10:21 创建
from queue import Queue
from functools import wraps

# 通过生成器和协程将回调函数内联到一个函数中
def apply_async(func, args, *, callback):
    result=func(*args)
    callback(result)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        # 初始时使用None来启动生成器
        result_queue.put(None)
        while True:
            print('1' * 15)
            result = result_queue.get()
            print('2' * 15)
            try:
                # 不断将计算结果发给生成器，产生下一次yield，使用a获取Async实例
                print('3' * 15)
                print('result={}'.format(result))
                a = f.send(result)
                print('4' * 15)
                # 异步计算， 回调使用put方法将结果放入队列中，之后send给等号左边
                apply_async(a.func, a.args, callback=result_queue.put)
                print('5' * 15)
            except StopIteration:
                print('end')
                break
    return wrapper

def add(x, y):
    return x + y

@inlined_async
def test():
    print('sss')
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('nihao', '-hello'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Bye')


def test_1():
    apply_async(add, (2, 3), callback=print)
    apply_async(add, ('hello', '-nihao'), callback=print)
    for n in range(10):
        apply_async(add, (n, n), callback=print)



if __name__ == '__main__':
    # import multiprocessing
    # pool =multiprocessing.Pool()
    # apply_async = pool.apply_async

    # 先运行装饰器中的 while send（None）启动生成器
    # 运行test， 将第一个Async实例传给 循环中的a
    # 异步计算 add（2,3）回调函数将结果放入队列
    # 继续运行循环体，获取结果（5） 发给生成器，获取下一个yield，第一次yield的r接收5
    # 第二个 yield 传输Async实例给a 异步计算结果，获取结果 发送给 第二个r，获取下一个yield
    # 没有yield ，结束
    test()
