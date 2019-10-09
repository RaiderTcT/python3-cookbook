#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 编码/解码Base64
Desc : 
"""
import base64


def codec_base64():
    # 编码和解码的结果都是bytes 或bytearray类型
    s = b"Hello World"
    a = base64.b64encode(s)  # 只能处理字节串和字节数组
    print(a)  # b'SGVsbG8gV29ybGQ='

    s_1 = bytearray(b'hello')
    print(s_1)  # bytearray(b'hello')
    a_1 = base64.b64encode(s_1)
    print(a_1, a_1.decode('ascii'))  # b'aGVsbG8=' aGVsbG8=

    print(base64.b64decode(a).decode('utf-8'))  # Hello World

if __name__ == '__main__':
    codec_base64()
