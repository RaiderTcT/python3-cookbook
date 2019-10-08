#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 增加/修改已打开文件的编码
Desc : 
"""
import urllib.request
import io
import sys
"""
TextIOWrapper
BufferWriter/Reader
FileIO
"""

def change_code():
    filename = "jalapeño.txt"

    f = open(filename, 'w')
    # 将最上层TextIOWrapper分离开， 返回Buffer层
    b = f.detach()
    print(f, b)
    # f.write('hello world\n')  ValueError: underlying buffer has been detached
    # <_io.TextIOWrapper mode='r' encoding='cp936'> <_io.BufferedReader name='jalapeño.txt'>
    f_new = io.TextIOWrapper(b, encoding='utf-8')
    print(f_new)
    print(f_new.write('HELLO WORLD\n'))
    f_new.close()


def change_open_encode():
    u = urllib.request.urlopen('http://www.python.org')
    f = io.TextIOWrapper(u, encoding='utf-8')
    text = f.read()

    print(sys.stdout.encoding)
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
    print(sys.stdout.encoding)

    f = open('sample.txt','w')
    print(f)
    print(f.buffer)
    print(f.buffer.raw)


if __name__ == '__main__':
    change_open_encode()
