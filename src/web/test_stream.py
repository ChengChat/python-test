import time

import requests
import json

from src.util.pretty_print import Pretty_Print

Pp = Pretty_Print()

# 目标接口的URL
url = 'http://127.0.0.1:5000/api/text_stream'

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'accept': 'text/event-stream',
}

# 发送POST请求
response = requests.get(url, headers=headers, stream=True)

# 检查请求是否成功
    # 获取响应内容
stream = response.content
# 解析响应内容
for line in stream.splitlines():
    if line:
        print(line)
