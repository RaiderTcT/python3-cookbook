# -*- coding: utf-8 -*-
# @作者     ： Ulysses
# @功能描述 ： 使用元类读取嵌套二进制结构
# @修改记录 ： 2019/1/31 16:25 创建
import struct


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


class StructureMeta(type):
    """
    使用元类来自动创建StructFiled 描述符
    元类是创建类的类，type是Python 的内建元类
    元类只会在该类被创建时才能做出响应，只能修改类属性，不会影响类的实例属性
    """
    def __init__(self, clsname, bases, clsdict):
        """
        创建类（Structure）时调用的初始化函数
        :param clsname: 要创建的类的名称
        :param bases: 基类、父类
        :param clsdict: 类属性
        """
        fields = getattr(self, '_fields_', [])  # 获取类属性_fields_
        # self是被创建的类实例， Structure和其子类PolyHeader
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<', '>', '!', '@')):
                byte_order = format[0]  # 字节序
                format = format[1:]
            format = byte_order + format
            # 在创建的类中添加 对应的StructField属性
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)  # 文件头大小
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'field_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num'),
    ]

if __name__ == '__main__':
    with open('polys.bin', 'rb') as f:
        phead = PolyHeader.from_file(f)
        print(phead.min_x, phead.num)
