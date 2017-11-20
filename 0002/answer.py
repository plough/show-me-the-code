#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql.cursors
import uuid


def main():
    conn = pymysql.connect(host='localhost',
                         user='root',
                         passwd='root',
                         db='show_me_the_code',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)

    try:
        with conn.cursor() as cursor:
            init_table(cursor)
            sql = "INSERT INTO `ActivationCode` (`code`) VALUES (%s)"
            code_list = get_activation_code_list()
            for code in code_list:
                print(code)
                cursor.execute(sql, (code,))
        conn.commit()
    finally:
        conn.close()


def init_table(cursor):
    # 如果数据表已经存在使用 execute() 方法删除表。
    cursor.execute("DROP TABLE IF EXISTS ActivationCode")
    # 创建数据表SQL语句
    sql = """CREATE TABLE ActivationCode (
                `id` INT NOT NULL AUTO_INCREMENT,
                `code` VARCHAR(50) NOT NULL,
                PRIMARY KEY(`id`)
                )
            """
    cursor.execute(sql)


def get_activation_code_list():
    result = []
    for i in range(200):
        result.append(str(uuid.uuid4()))
    return result


if __name__ == "__main__":
    main()
