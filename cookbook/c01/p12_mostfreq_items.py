#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
序列中出现次数最多的元素， Counter
一个 Counter 是一个 dict 的子类，用于计数可哈希对象。
它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值。
计数可以是任何整数值，包括0和负数。
"""
from collections import Counter


words = """A Counter is a dict subclass for counting hashable objects.
    It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
    Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags
    or multisets in other languages.
    """
gen_1  = (item for item in range(1, 10))


cnt = Counter(gen_1)
for k, v in cnt.items():
    print(k, v)
print(cnt)  # 每个字符出现的次数
print(cnt.most_common(3))  # 出现频率最高的3个字符 [(' ', 69), ('e', 30), ('s', 25)]
print(cnt.most_common()[:-3:-1]) # 最低的2个字符
print(cnt['c'])  # c的出现次数
print(sum(cnt.values()))  # total


c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))
more_words = ['c', 'd', 'c']
c.update(more_words)
print(c)
print(+c)  # remove zero and negative counts
# 单目加和减（一元操作符）意思是从空计数器加或者减去。
print(-c)

print("="*30)
cnt_1 = Counter(a=3, b=2, c=1)
cnt_2 = Counter(a=1, b=3, c=2)

print(cnt_1 + cnt_2)  # cnt_1[x] + cnt_2[x]
print(cnt_1 - cnt_2)  # 相减 只保留正数
print(cnt_1 & cnt_2)  # intersection:  min(cnt_1[x], cnt_2[x]) # doctest: +SKIP
print(cnt_1 | cnt_2)  # union max(cnt_1[x], cnt_2[x])

print("="*30)

def most_freqency():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    from collections import Counter
    word_counts = Counter(words)
    # 出现频率最高的3个单词
    top_three = word_counts.most_common(3)
    print(top_three)
    # Outputs [('eyes', 8), ('the', 5), ('look', 4)]

if __name__ == '__main__':
    most_freqency()
