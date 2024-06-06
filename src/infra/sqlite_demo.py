import time
import requests
import sqlite3

# SQLite数据库文件名
DATABASE_FILE = '../../source/track.db'

# 创建或连接到SQLite数据库
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

cursor.execute('''
Alter table tokens add column `update_at` TIMESTAMP NOT NULL DEFAULT '2024-05-30 06:39:47'
''')
conn.commit()


def insert():
    try:
        # 发送请求来获取新的token
        new_token = 'demo-token'

        # 将新的token插入到数据库中
        cursor.execute('INSERT INTO tokens (token) VALUES (?)', (new_token,))
        conn.commit()
        print(f'Token refreshed and saved to SQLite database')
    except requests.exceptions.RequestException as e:
        print(f'Error refreshing token: {e}')

def select():
    try:
        # 将新的token插入到数据库中
        cursor.execute('select * from tokens')
        row = cursor.fetchone()

        # 如果查询到结果，打印token
        if row:
            latest_token = row[1]
            # print(f'最新的token是: {latest_token}')
        else:
            print('没有找到token。')
    except requests.exceptions.RequestException as e:
        print(f'Error refreshing token: {e}')


# insert()
#
# select()

# 关闭数据库连接
conn.close()

