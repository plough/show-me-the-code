#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import redis
import uuid
import pprint


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    code_list = get_activation_code_list()
    # 使用 redis 的集合
    r.delete('ActivationCodes')  # 先清空
    r.sadd('ActivationCodes', *code_list)  # 再插入
    # result 是一个包含所有查询数据的 set
    result = r.smembers('ActivationCodes')
    pprint.pprint(result)


def get_activation_code_list():
    result = []
    for i in range(200):
        result.append(str(uuid.uuid4()))
    return result


if __name__ == "__main__":
    main()
