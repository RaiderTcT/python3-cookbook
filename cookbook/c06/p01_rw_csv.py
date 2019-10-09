#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 读写CSV数据
Desc : 
"""
import csv
from collections import namedtuple


def rw_csv():
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            print(row)

    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            # Process row
            print(row.Change)

    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
    ]

    with open('stocks.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

    rows_1 = [
        {'Symbol': "AA", "Price": 33.21, "Date": '01/28/2019',
         'Time': '06:30pm', 'Change': 0.12, 'Volume': 33200},
        {'Symbol': "AIG", "Price": 43.21, "Date": '01/28/2019',
         'Time': '06:30pm', 'Change': 0.12, 'Volume': 11200},
        {'Symbol': "AXP", "Price": 53.21, "Date": '01/29/2019',
         'Time': '06:30pm', 'Change': 0.12, 'Volume': 13300},
    ]
    with open('stocks_1.csv', 'w') as f:
        f_csv = csv.DictWriter(f, fieldnames=headers)
        f_csv.writeheader()
        f_csv.writerows(rows_1)        

if __name__ == '__main__':
    rw_csv()

