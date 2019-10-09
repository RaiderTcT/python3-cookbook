#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Ulysses
@Date: 2019-01-03 20:49:57
@Description: XMLNameSpace 处理
@LastEditTime: 2019-10-09 10:47:46
'''
# -*- coding: utf-8  -*-
from xml.etree.ElementTree import parse


class XMLNamespaces:
    """将namespace映射为简单的key"""
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        """format-string处理xpath"""
        return path.format_map(self.namespaces)

if __name__ == "__main__":

    ns = XMLNamespaces(default="urn:schemas-microsoft-com:office:spreadsheet",
                    ss='urn:schemas-microsoft-com:office:spreadsheet')

    print(ns.namespaces, ns('{default}Worksheet/{ss}Table'))
    # {'default': '{urn:schemas-microsoft-com:office:spreadsheet}', 'ss': '{urn:schemas-microsoft-com:office:spreadsheet}'}
    # {urn:schemas-microsoft-com:office:spreadsheet}Worksheet/{urn:schemas-microsoft-com:office:spreadsheet}Table

    doc = parse('test.xml')
    root = doc.getroot()

    print(root.find('{urn:schemas-microsoft-com:office:spreadsheet}Styles'))
    print(root.find(ns('{default}Worksheet/{ss}Table')))
