import asyncio
import json

import aiohttp

from src.util.pretty_print import Pretty_Print

Pp = Pretty_Print()

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZTUxNGU4MDg4NmY0OWMwOTI5MGI0ZjZhYzdkZGVmNSIsImV4cCI6MTcxNzA1ODQ5OCwibmJmIjoxNzE2OTcyMDk4LCJpYXQiOjE3MTY5NzIwOTgsImp0aSI6ImMxYWZjZmM2Yzk1ZTQ0NTdhM2FkZjBmNGE4NWViMDkwIiwidWlkIjoiNjYwMTcyNDZlN2UxZTAxNWYzNDY4MDIyIiwidHlwZSI6ImFjY2VzcyJ9.nUzIEVxQJeJ21UiUv-uDiaxxajBDcCZdRCuNgnAK3a4',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'acw_tc=784e2c9417158561203907114e2970268ee86812441b79804f500c942d2926; _ga_PMD05MS2V9=GS1.1.1715856129.19.0.1715856129.0.0.0; chatglm_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNTg1NjE1MSwianRpIjoiYTQzNGY2MDctYWM2NS00Yjk1LTk1YWUtMDZlYjkxZTYwNDI2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImVlNTE0ZTgwODg2ZjQ5YzA5MjkwYjRmNmFjN2RkZWY1IiwibmJmIjoxNzE1ODU2MTUxLCJleHAiOjE3MTU5NDI1NTEsInVpZCI6IjY2MDE3MjQ2ZTdlMWUwMTVmMzQ2ODAyMiIsInVwbGF0Zm9ybSI6ImlPUyIsInJvbGVzIjpbInVuYXV0aGVkX3VzZXIiXX0.n4B1ECg6PPwgnSBgg8Q_Sn-tOcBuv1O5H-e-jCuxxYs;',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'accept': 'text/event-stream',
}

# 目标接口的URL
url = 'https://chatglm.cn/chatglm/backend-api/assistant/stream'

# 请求体
# question = "1+1"
question = "你叫什么"

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


async def sse_client():
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers,
                                data=json.dumps(payload)) as response:
            while True:  # 可以在这里添加逻辑来处理接收到的数据
                try:
                    data = await response.content.readline()
                    if not data:
                        break
                    data_str = data.decode('utf-8').strip()
                    if data_str:
                        if data_str == 'event:message':
                            continue
                        line_json = data_str.split("data: ")[1]
                        data = json.loads(line_json)
                        if len(data['parts']) > 0:
                            if len(data['parts'][0]['content']) > 0:
                                text_ = data['parts'][0]['content'][0]['text']
                                # print(text_)
                                print(Pp.loadingPrinting("回复: " + text_),
                                      end="",
                                      flush=True)

                except asyncio.CancelledError:
                    break

asyncio.run(sse_client())
