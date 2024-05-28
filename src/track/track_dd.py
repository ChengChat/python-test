import ssl

import aiohttp
import asyncio
import json

from aiohttp import TCPConnector


async def make_request():
    url = 'https://chatglm.cn/chatglm/backend-api/assistant/stream'
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'Bearer your_actual_token_here', # 使用实际的token替换
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 请将下面的Cookie替换为实际的cookie字符串
        'Cookie': 'your_actual_cookie_here',
        'Origin': 'https://chatglm.cn',
        'Referer': 'https://chatglm.cn/main/alltoolsdetail',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'accept': 'text/event-stream',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    payload = {
        "assistant_id": "65940acff94777010aa6b796",
        "conversation_id": "66502c865cc0b0919f1fa1ff",
        "meta_data": {
            "mention_conversation_id": "",
            "is_test": False,
            "input_question_type": "xxxx",
            "channel": "",
            "draft_id": "",
            "quote": "",
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "wef "
                    }
                ]
            }
        ]
    }

    # 创建一个 TCPConnector 实例，如果需要禁用 SSL 证书验证，可以在这里设置
    connector = TCPConnector(ssl_context=ssl.create_default_context())
    async with aiohttp.ClientSession(connector=connector) as session:
        connector = aiohttp.TCPConnector(ssl=False)
        async with session.post(url, headers=headers, data=json.dumps(payload)) as response:
            while True:  # 可以在这里添加逻辑来处理接收到的数据
                if response.closed:
                    break
                data = await response.text()
                print(data)  # 打印接收到的数据，或者进行其他处理

asyncio.run(make_request())

