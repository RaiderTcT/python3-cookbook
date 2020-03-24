# 斐波那契函数
#
import time

# n = 35 ,7.1s
# 时间复杂度： O(1.6^n) 指数阶


def fib_1(n):
    if n < 2:
        return 1
    else:
        return fib_1(n - 1) + fib_1(n - 2)


# n = 35, 0.2s
# 时间复杂度 O(n) 线性阶


def fib_2(n):
    f1 = f2 = 1
    for k in range(1, n):
        f1, f2 = f2, f1 + f2
    return f2


# 返回的是iterable 对象
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


if __name__ == "__main__":
    print(time.ctime())
    for n in fab(35):
        print(n)
    print(time.ctime())
