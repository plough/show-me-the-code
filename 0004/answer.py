#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import pprint
from collections import Counter


'''
1. 缩写单独视为一个单词，例如 You're 和 you，are 是不同的单词；I'm 与 I，am 是不同的单词。
2. 统一转换为小写
'''
def main():
    with open('zen_of_python.txt') as f:
        origin_text = f.read()
    wordpat = re.compile(r"([a-zA-Z]+([-|'][a-zA-Z]+)?)")
    wordlist = [item[0].lower() for item in wordpat.findall(origin_text)]
    wordcount = Counter(wordlist)
    result = [(k, v) for k, v in wordcount.items()]
    result.sort(key=lambda x: x[1], reverse=True)
    pprint.pprint(result)


if __name__ == "__main__":
    main()
