# -*- coding: utf-8 -*-
# @作者     ： Ulysses
# @功能描述 ： 读取嵌套和大小可变的二进制结构
# @修改记录 ： 2019/1/31 12:24 创建
import struct
import itertools
"""
文件头
0x1234
min_x
min_y
max_x
max_y
数量

记录长度
记录
points
"""
polys = [
    [(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
    [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
    [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
]


def write_polys(filename, polys):
    # 将polys解为一个序列
    flattened = list(itertools.chain(*polys))
    max_x = max(x for x, _ in flattened)
    min_x = min(x for x, _ in flattened)
    max_y = max(y for _, y in flattened)
    min_y = min(y for _, y in flattened)
    print(max_x, max_y, min_x, min_y)

    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi', 0x1234,
                            min_x, min_y,
                            max_x, max_y, len(polys)))

        for poly in polys:
            size = len(poly) * struct.calcsize('<dd') # 记录长度
            f.write(struct.pack('<i', size+4))  # 记录+ 记录长度（4字节）
            for pt in poly:
                f.write(struct.pack('<dd', *pt))  # 写入元组


class StructField:
    """
    描述符，代表每一个结构字段 二进制结构文件 文件头
    """
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, owner):
        if not instance:  # 被用来访问属性的实例
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class Structure:
    def __init__(self, bytedata):
        # 返回由给定实参创建的“内存视图”对象
        # memoryview对象允许Python代码访问支持缓冲区协议的对象的内部数据而无需复制。
        self._buffer = memoryview(bytedata)


class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num = StructField('<i', 36)


if __name__ == '__main__':
    write_polys('polys.bin', polys)
    with open('polys.bin', 'rb') as f:
        phead = PolyHeader(f.read(40))
        print(phead.max_x, phead.num, hex(phead.file_code))
