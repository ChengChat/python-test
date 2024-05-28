import time

import requests
import json

from src.util.pretty_print import Pretty_Print

Pp = Pretty_Print()

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZTUxNGU4MDg4NmY0OWMwOTI5MGI0ZjZhYzdkZGVmNSIsImV4cCI6MTcxNjYzMTk3NywibmJmIjoxNzE2NTQ1NTc3LCJpYXQiOjE3MTY1NDU1NzcsImp0aSI6ImNlYTUxODk1MTI5NzRjZGZhNTFiYzgxY2FmOGU1NjVjIiwidWlkIjoiNjYwMTcyNDZlN2UxZTAxNWYzNDY4MDIyIiwidHlwZSI6ImFjY2VzcyJ9.UWdMSQHLcLCNt5rk-7EAXjKXrh9ar8569Xn8NOddHxY',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'acw_tc=784e2c9417158561203907114e2970268ee86812441b79804f500c942d2926; _ga_PMD05MS2V9=GS1.1.1715856129.19.0.1715856129.0.0.0; chatglm_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNTg1NjE1MSwianRpIjoiYTQzNGY2MDctYWM2NS00Yjk1LTk1YWUtMDZlYjkxZTYwNDI2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVlNTE0ZTgwODg2ZjQ5YzA5MjkwYjRmNmFjN2RkZWY1IiwibmJmIjoxNzE1ODU2MTUxLCJleHAiOjE3MTU5NDI1NTEsInVpZCI6IjY2MDE3MjQ2ZTdlMWUwMTVmMzQ2ODAyMiIsInVwbGF0Zm9ybSI6ImlPUyIsInJvbGVzIjpbInVuYXV0aGVkX3VzZXIiXX0.n4B1ECg6PPwgnSBgg8Q_Sn-tOcBuv1O5H-e-jCuxxYs;',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'accept': 'text/event-stream',
}

# 目标接口的URL
url = 'https://chatglm.cn/chatglm/backend-api/assistant/stream'

# 请求体
question = "1+1"

payload = {
    "assistant_id": "65940acff94777010aa6b796",
    "conversation_id": "663ee9002b28b09032b58503",
    "meta_data": {
        "mention_conversation_id": "",
        "is_test": False,
        "input_question_type": "xxxx",
        "channel": "",
        "draft_id": ""
    },
    "messages": [
        {"role": "user", "content": [{"type": "text", "text": question}]}
    ]
}

print("问题: ", question)

# 发送POST请求
response = requests.post(url, json=payload, headers=headers, stream=True)

# 检查请求是否成功
if response.status_code == 200:
    # 获取响应内容
    stream = response.text
    # 解析响应内容
    for line in stream.splitlines():
        if line:
            # 解析JSON数据
            # print(line)
            if line == 'event:message':
                continue
            line_json = line.split("data: ")[1]
            data = json.loads(line_json)
            # print(data)
            if len(data['parts']) > 0:
                if len(data['parts'][0]['content']) > 0:
                    text_ = data['parts'][0]['content'][0]['text']
                    print(Pp.loadingPrinting("回复: " + text_), end="", flush=True)
                    time.sleep(0.1)  # 模拟耗时操作


else:
    print("Error:", response)
