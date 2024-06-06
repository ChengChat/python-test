import time
import requests
import sqlite3

# SQLite数据库文件名
DATABASE_FILE = '../../source/track.db'

def update(name, token, refresh_token):
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            # 将新的token插入到数据库中
            cursor.execute(
                'UPDATE tokens SET token = ?, refresh_token = ?, update_at = CURRENT_TIMESTAMP WHERE name = ?',
                (token, refresh_token, name))
            conn.commit()
            print(f'Token refreshed and saved to SQLite database')
    except requests.exceptions.RequestException as e:
        print(f'Error refreshing token: {e}')


def select(name):
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            # 将新的token插入到数据库中
            cursor.execute('select * from tokens where name = ?', (name, ))
            row = cursor.fetchone()

            # 如果查询到结果，打印token
            if row:
                latest_token = row[2]
                # print(f'最新的token是: {latest_token}')
                return latest_token
            else:
                print('没有找到token。')
    except requests.exceptions.RequestException as e:
        print(f'Error refreshing token: {e}')

