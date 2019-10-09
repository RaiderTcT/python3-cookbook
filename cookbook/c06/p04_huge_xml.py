#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8  -*-
"""
使用增量方式解析大型xml文件
"""
from xml.etree.ElementTree import iterparse
from xml_namespace import XMLNamespaces

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    # 增量式处理， 提供文件名和事件列表（start/end）
    parse = iterparse(filename, ("start", "end"))

    next(parse)  # 跳过了root元素
    tag_stack = []
    elem_stack = []
    for event, elem in parse:  # 生成(event, elem)的元组
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)  # 从父节点中移除当前元素
            try:
                elem_stack.pop()  # 相应地从栈中移除yield返回的元素
                tag_stack.pop()  # 等待下一个需要的element
            except IndexError:
                pass


ns_1 = XMLNamespaces(default="urn:schemas-microsoft-com:office:spreadsheet",
                    o="urn:schemas-microsoft-com:office:office",
                    x="urn:schemas-microsoft-com:office:excel",
                    dt="uuid:C2F41010-65B3-11d1-A29F-00AA00C14882",
                    ss="urn:schemas-microsoft-com:office:spreadsheet")

data = parse_and_remove("test.xml",
                         ns_1('{x}ExcelWorkbook/{x}WindowHeight'))
data_1 = parse_and_remove("test.xml",
        ns_1("{ss}Worksheet/{ss}Table/{ss}Row/{ss}Cell/{ss}Data"))

for item in data_1:
    print(item.text)




def huge_xml():
    potholes_by_zip = Counter()

    doc = parse('potholes.xml')
    for pothole in doc.iterfind('row/row'):
        potholes_by_zip[pothole.findtext('zip')] += 1
    for zipcode, num in potholes_by_zip.most_common():
        print(zipcode, num)


    potholes_by_zip = Counter()

    data = parse_and_remove('potholes.xml', 'row/row')
    for pothole in data:
        potholes_by_zip[pothole.findtext('zip')] += 1
    for zipcode, num in potholes_by_zip.most_common():
        print(zipcode, num)

if __name__ == '__main__':
    huge_xml()

